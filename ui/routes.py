from flask import render_template, request, redirect, url_for
from ui import app, db, forms, recordings
from ui.models import *
from ui.forms import *
import datetime, re
from sqlalchemy.orm import joinedload, raiseload

@app.route('/')
def index():
	user = {'username': 'DefaultUser'}
	return render_template('index.html', title='Home', user=user)

@app.route('/lineup/<date>')
@app.route('/lineup', methods=['GET', 'POST'])
def lineup(date=None):
	if date == None:
		date = datetime.datetime.today().strftime('%Y-%m-%d')
	airings = []
	if request.method == 'POST':
		query = request.form['query']
		programs = Program.query.filter( Program.title.like("%"+query+"%")  | Program.episodeTitle.like("%"+query+"%") | Program.description.like("%"+query+"%")).all()
		for program in programs:
			airings.extend(program.airings)

	if request.method == 'GET':
		start = int(datetime.datetime.strptime(date, "%Y-%m-%d").timestamp())
		stop = start + 86400
		airings = Airing.query.filter(Airing.airDateTime >= start, Airing.airDateTime < stop).all()

	dates = []
	for i in range(-1, 14):
		today = datetime.datetime.today()
		today += datetime.timedelta(days=i)
		dates.append(today.strftime('%Y-%m-%d'))

	return render_template('lineup.html', airings=airings, date=date, dates=dates, title="Lineup")




@app.route('/recordings', methods=['GET'])
def list_recordings():
	recordings = ScheduledRecording.query.all()
	return render_template('record_list.html', recordings=recordings, title="Manage Recording")


@app.route('/record/delete/<programID>', methods=['GET'])
def delete_recording(programID):
	recording = ScheduledRecording.query.filter_by(programID=programID).one()
	db.session.delete(recording)
	db.session.commit()
	recordings.update()
	return redirect(url_for('list_recordings'))


@app.route('/record/<programID>', methods=['GET', 'POST'])
def record(programID):

	stationID=request.args.get('stationID')
	airDateTime=request.args.get('airDateTime')
	
	print(programID, stationID, airDateTime)

	if request.method == 'POST':
		recording = ScheduledRecording.query.filter_by(programID=programID).one()
		form = RecordForm(request.form, obj=recording)
		form.populate_obj(recording)

		if recording.series:
			recording.programID = programID[:10]
		else:
			recording.new = False

		db.session.commit()
		recordings.update()
		return redirect(url_for('list_recordings'))
		
	if request.method == 'GET':
		recording = ScheduledRecording.query.filter_by(programID=programID).one_or_none()

		if not recording:
			airing = Airing.query.filter_by(stationID=stationID, airDateTime=airDateTime).one()
			program = Program.query.filter_by(programID=programID).one()
			recording = ScheduledRecording(programID=programID)
			recording.series = False #bool(re.match('^EP', programID))
			recording.new_only = recording.series
			recording.title = program.title
			recording.prefer_station = airing.station
			recording.any_station = get_setting('any_station') or False
			recording.priority = get_setting('priority') or 0
			recording.start_padding = get_setting('start_padding') or 0
			recording.stop_padding = get_setting('stop_padding') or 0

			if recording.series:
				recording.programID = programID[:10]

			db.session.add(recording)
			db.session.commit()

		form = RecordForm(obj=recording)
		form.fullID.data = programID
		
	recordings.update()
	return render_template('record.html', recording=recording, title="Manage Recording", form=form)
