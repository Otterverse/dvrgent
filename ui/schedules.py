import hashlib, logging
from ui import app, db, recordings
from ui.models import *
from schedulesdirect.schedulesdirect import *
from sqlalchemy.orm import joinedload, raiseload
from sqlalchemy import text

def login():

	SD = SchedulesDirect()
	SD.token = SD.api_login(get_setting('username'), get_setting('password'))
	set_setting('token', SD.token)
	db.session.commit()
	return SD

def update_stations(SD):
	data = SD.api_get_stations(get_setting('lineup'))

	for new_station in data['stations']:
		station = Station.query.filter_by(stationID=new_station.get('stationID')).one_or_none() or Station(stationID=new_station.get('stationID'), enabled=1)
		db.session.add(station)
		station.name = new_station.get('name')
		station.callsign = new_station.get('callsign')
		station.affiliate = new_station.get('affiliate')

	mapped_stations = []
	for mapping in data['map']:
		station = Station.query.filter_by(stationID=mapping.get('stationID')).one()

		if station.stationID in []:
			station.airings.clear()
			station.schedules.clear()
			logging.debug("Skipping ID %s", station.stationID)
			db.session.delete(station)
			continue

		old_station = Station.query.filter_by(channel=mapping.get('channel')).one_or_none()

		if old_station:
			station.enabled = old_station.enabled
			station.airings = old_station.airings
			station.schedules = old_station.schedules
			old_station.channel = int(old_station.channel) + 10000
			db.session.commit()

		station.channel = mapping.get('channel')
		mapped_stations.append(station)
		logging.debug(station)
	timestamp = sd_timestamp_to_unix(data['metadata'].get('modified'))
	set_setting("lineup_modified", timestamp)

	for station in Station.query.all():
		if (station not in mapped_stations):
			logging.debug("DELETING: ", station)
			station.airings.clear()
			station.schedules.clear()
			db.session.delete(station)

	db.session.commit()


def update_airings(SD):

	#Clean up after disabled stations
	for station in Station.query.filter_by(enabled=False).all():
		for schedule in station.schedules:
			logging.debug("DELETING: ", schedule)
			db.session.delete(schedule)
		for airing in station.airings:
			logging.debug("DELETING: ", airing)
			db.session.delete(airing)

	db.session.commit()

	station_list = Station.query.filter_by(enabled=True).all()
	stationIDs = []
	for station in station_list:
		stationIDs.append({"stationID": station.stationID})

	new_md5s = SD.api_get_schedule_md5s(stationIDs)

	schedule_update_request = []
	for station in stationIDs:
		stationID = station['stationID']
		station_update = {'stationID': stationID, 'date': [] }

		if new_md5s[stationID] == []:
			logging.warning("No updates available for stationID: %s" % stationID)
			continue

		for date in new_md5s[stationID].keys():
			new_md5 = new_md5s[stationID][date]['md5']
			sched = Schedule.query.filter_by(stationID=stationID, date=date).one_or_none()
			if sched:
				old_md5 = sched.md5
			else:
				old_md5 = None
			
			if(new_md5 != old_md5):
				logging.debug("New: %s Old: %s Station: %s" % (new_md5, old_md5, stationID))
				station_update['date'].append(date)

		if station_update['date']:
			schedule_update_request.append(station_update)

	if not schedule_update_request:
		return

	schedule_updates = SD.api_get_schedules(schedule_update_request)

	for update in schedule_updates:
		stationID = update['stationID']
		startDate = sd_timestamp_to_unix(update['metadata']['startDate'])
		endDate = startDate + 86400

		Airing.query.filter(Airing.stationID == stationID, Airing.airDateTime >= startDate, Airing.airDateTime < endDate).delete()

		#Need to watch for duplicate times because we can't trust the API
		seen_times = []

		for program in update['programs']:
			new = False
			try:
				if (program['new']):
					new = True
			except:
				pass

			airing = Airing(
				stationID=stationID,
				programID=program['programID'],
				airDateTime=sd_timestamp_to_unix(program['airDateTime']),
				duration=program['duration'],
				new=new,
				md5=program['md5']
			)

			if airing.airDateTime not in seen_times:
				db.session.add(airing)
				seen_times.append(airing.airDateTime)

			else:
				logging.warning("Duplicate!!")
				logging.warning(airing)

			logging.debug(airing)


		schedule = Schedule.query.filter_by(stationID=stationID, date=update['metadata']['startDate']).one_or_none() or Schedule(stationID=stationID, date=update['metadata']['startDate'])

		schedule.lastModified = sd_timestamp_to_unix(update['metadata']['modified'])
		schedule.md5 = update['metadata']['md5']
		db.session.add(schedule)
		logging.debug(schedule)
		db.session.commit()




def update_programs(SD):

	n = 0

	all_airings = Airing.query.from_statement(text('SELECT airing."stationID" AS "airing_stationID", airing."programID" AS "airing_programID", airing."airDateTime" AS "airing_airDateTime", airing.duration AS airing_duration, airing.new AS airing_new, airing.md5 AS airing_md5, airing.recording_id AS airing_recording_id FROM airing where airing.airDateTime > strftime("%s","now")-86400 AND (airing.programID not in (select program.programID from program) OR airing.md5 != (select program.md5 from program where program.programID = airing.programID))')).all()

	#Run up to 50 batches
	while n < 50:
		n=n+1
		logging.debug("Batch number %s" % n)

		program_update_request = []

		while len(all_airings) > 0:
			airing = all_airings.pop()
			program_update_request.append(airing.programID)

			#Limit batch size to 2500
			if (len(program_update_request) >= 2500):
				break


		if not program_update_request:
			break

		programs_update = SD.api_get_programs(program_update_request)

		#Process a batch

		for new_program in programs_update:

			if (int(new_program.get("code") or 0) > 0):
				continue

			program = Program.query.filter_by(programID=new_program.get('programID')).one_or_none() or Program(programID=new_program.get('programID'))

			program.entityType = new_program.get('entityType')
			program.title = new_program['titles'][0].get('title120')
			program.episodeTitle = new_program.get('episodeTitle150')
			program.originalAirDate = new_program.get('originalAirDate')
			program.md5 = new_program.get('md5')

			try:
				program.description = new_program['descriptions']['description100'][0].get('description')
			except KeyError:
				pass

			try:
				program.longDescription = new_program['descriptions']['description1000'][0].get('description')
			except KeyError:
				pass

			if(program.entityType == "Episode"):
				try:
					for key in new_program['metadata'][0]:
						season = new_program['metadata'][0][key].get('season')
						episode = new_program['metadata'][0][key].get('episode')
						if (season > 0 or episode > 0):
							program.season_episode = "%01dx%02d" % (int(season), int(episode))
							break
				except KeyError:
					pass

			db.session.add(program)
			logging.debug(program)

		db.session.commit()

	#Clean up orphaned programs
	for program in Program.query.from_statement(text('SELECT program."programID" AS "program_programID", program."entityType" AS "program_entityType", program.title AS program_title, program."episodeTitle" AS "program_episodeTitle", program.description AS program_description, program."longDescription" AS "program_longDescription", program."originalAirDate" AS "program_originalAirDate", program.season_episode AS program_season_episode, program.md5 AS program_md5 FROM program where program.programID not in (select distinct airing.programID from airing)')).all():
		logging.debug("DELETING: %s" % program)
		db.session.delete(program)

	db.session.commit()


def fetch_updates():
	#Login and get status
	SD = login()
	status = SD.api_status()
	if (status['system'] != "Online"):
		logging.warning(status)
		return(False)

	#Station lineup is part of main status
	if (status['lineup_modified'] > int(get_setting('lineup_modified') or 0)):
		update_stations(SD)

	#Main update loops
	update_airings(SD)
	update_programs(SD)
	recordings.update()
