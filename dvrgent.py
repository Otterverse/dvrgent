#!/usr/bin/python3

from hdhomerun.hdhomerunprime import *
from ui import app, db, recordings, schedules
from ui.models import *
from threading import Timer
import time, logging, os
from sqlalchemy import exc


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s',)


last_check = int(get_setting('last_update') or 0)
update_interval = int(get_setting('update_interval') or 21600)

last_loop = 0
loop_delay = 15

recorders = []

active_jobs = []

def get_recorder(channel=None):
	global recorders

	for recorder in recorders:
		if recorder.channel == channel:
			return recorder

	rec = MultiRecorder(channel=channel)
	recorders.append(rec)
	return rec


def job_start(job_id):

	global active_jobs

	job = RecordingJob.query.filter_by(programID=job_id).one()
	try:
		job.active = True
		db.session.commit()

		while (time.time() < job.start_time + 300):
			try:
				rec = get_recorder(job.channel)
				if rec.start():
					fp = open(job.filename, 'wb')
					rec.add_file(fp)
					t_stop = Timer(job.start_time - time.time() + job.duration, job_stop, [job.programID])
					t_stop.start()
					active_jobs.append(t_stop)
					logging.info("Start: %s", job)
					return True
			except:
				time.sleep(1)

		job.active = False
		db.session.commit()
		logging.info("Could not start job: %s", job)

	except exc.OperationalError:
		logging.exception("Error writing to DB during job_start!")
		db.session.rollback()

def job_stop(job_id):
	job = RecordingJob.query.filter_by(programID=job_id).one()
	logging.info("Stop: %s", job)
	try:
		rec = get_recorder(job.channel)
		rec.end_file()
		job.active = False
		job.complete = True

		#We got the episode/show, so clear this and any other scheduled tries on it.
		airings = Airing.query.filter_by(programID=job_id).all()
		for airing in airings:
			airing.recording_id = None

		db.session.commit()
	except exc.OperationalError:
		logging.exception("Error writing to DB during job_stop!")
		db.session.rollback()






def schedule_new_jobs():
	global active_jobs

	airings = Airing.query.filter(Airing.recording_id != None, Airing.airDateTime > time.time(), Airing.airDateTime < (time.time() + loop_delay * 20)).all()

	if airings:
		airings = sorted(airings, key=lambda airing: airing.scheduled_recording.priority)


	schedule_time = time.time()

	for airing in airings:
		#Create job
		job = RecordingJob.query.filter_by(programID=airing.programID).one_or_none()
		if job:
			continue
		job = RecordingJob()
		job.programID = airing.programID
		job.title = airing.program.title
		job.episodeTitle = airing.program.episodeTitle
		job.season_episode = airing.program.season_episode
		job.channel = airing.station.channel

		#Directory for each series
		temp_dir = (get_setting('save_path') or "/tmp") + '/' + ('Movies' if (airing.program.entityType != 'Episode') else "TV/" + job.title.replace('/','_').replace('?','').replace(':',''))

		if not os.path.exists(temp_dir):
			os.makedirs(temp_dir, 0o755)

		#Format filename
		if airing.program.entityType == 'Episode':
			temp_filename = job.title + " - " + (job.season_episode or '#x##') + " - " + (job.episodeTitle or '#####') + ".mpegts"
		else:
			temp_filename = job.title + ".mpegts"
		temp_filename = temp_filename.replace('/','-').replace('?','').replace(':','')
		job.filename = temp_dir + '/' + temp_filename

		if os.path.exists(job.filename):
			job.filename = job.filename + '_' + str(airing.airDateTime)

		job.start_time = airing.airDateTime - airing.scheduled_recording.start_padding
		job.duration = airing.duration + airing.scheduled_recording.start_padding + airing.scheduled_recording.stop_padding
		job.station = airing.station
		job.new = airing.new
		job.priority = airing.scheduled_recording.priority
		job.active = False
		job.complete = False

		db.session.add(job)
		db.session.commit()

		t_start = Timer(job.start_time - time.time() + time.time() - schedule_time, job_start, [job.programID])
		t_start.start()

		active_jobs.append(t_start)



		logging.info("New: %s - %s", job, job.filename)
		time.sleep(1)




def cleanup():
	for job in RecordingJob.query.filter_by(complete=True).all():
		schedule = ScheduledRecording.query.filter_by(programID=job.programID).one_or_none()
		#If we got a schedule, it has to be a full length (non-series) show ID, meaning a one-shot
		if schedule:
			db.session.delete(schedule)
		db.session.delete(job)

	#Catch dead/failed jobs that never got marked complete. Explicit episodes and regular series should automatically reschedule.
	for job in RecordingJob.query.filter_by(complete=False).filter(RecordingJob.start_time + RecordingJob.duration < time.time()-300).all():
		schedule = ScheduledRecording.query.filter_by(programID=job.programID).one_or_none()
		if not schedule and job.new:
			#If a "first run only" series recording failed, add an episode-specific schedule for the missed episode (since it will no longer be "first run.")
			replacement_schedule = ScheduledRecording()
			replacement_schedule.programID = job.programID
			replacement_schedule.stationID = job.stationID
			replacement_schedule.title = job.title
			replacement_schedule.priority = job.priority
			replacement_schedule.start_padding = get_setting('start_padding') or 0
			replacement_schedule.stop_padding = get_setting('stop_padding') or 0
			db.session.add(replacement_schedule)
			logging.info("Rescheduling: %s", job)

		db.session.delete(job)

	db.session.commit()


def reaper():
	global recorders
	new_recorders = []
	for rec in recorders:
		if rec.should_run:
			new_recorders.append(rec)
	recorders = new_recorders

	global active_jobs
	new_jobs = []
	for job in active_jobs:
		if job.is_alive():
			new_jobs.append(job)
	active_jobs = new_jobs





while True:
	#Schedule updates are less frequent
	if time.time() > last_check + update_interval:
		logging.info("Fetching schedule update")
		try:
			schedules.fetch_updates()
			last_check = int(time.time())
			set_setting('last_update', last_check)
			logging.info("Schedule update complete")

		except:
			last_check += 1800
			set_setting('last_update', last_check)
			logging.exception("Error fetching update!")

	try:
		#Axe the done jobs
		reaper()
		cleanup()
		schedule_new_jobs()
	except exc.OperationalError:
		logging.exception("Error writing to DB during main loop!")
		db.session.rollback()
	except:
		logging.exception("Error in maintenance tasks!")


	time.sleep(loop_delay)


