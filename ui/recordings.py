from ui import app, db
from ui.models import *
import time, logging
from sqlalchemy import or_

def update():

	for recording in ScheduledRecording.query.all():

		recording.airings.clear()

		if recording.series:
			airings = Airing.query.filter_by(stationID=recording.stationID).filter(Airing.programID.like(recording.programID+'%'))
			if recording.new_only:
				airings = airings.filter_by(new=True)
			airings = airings.order_by('airDateTime')
		else:
			airings = Airing.query.filter_by(stationID=recording.stationID).filter_by(programID=recording.programID)

		airings = airings.filter(Airing.airDateTime > time.time()).order_by('airDateTime')


		for airing in airings.all():
			recording.airings.append(airing)
			if not recording.series:
				break

	for airing in Airing.query.filter(Airing.recording_id != None, or_(Airing.scheduled_recording == None, Airing.airDateTime < time.time())).all():
		logging.debug(airing)
		airing.recording_id = None

	db.session.commit()