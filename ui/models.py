from ui import db

class Setting(db.Model):
	key = db.Column(db.String(64), primary_key=True)
	value = db.Column(db.String(256))

	def __repr__(self):
		return '<Setting: {} = {}>'.format(self.key, self.value)

def get_setting(name):
	setting = Setting.query.filter_by(key=name).one_or_none()
	if setting:
		return setting.value or None

def set_setting(name, value):
	setting = Setting.query.filter_by(key=name).one_or_none()
	if (setting == None):
		if (value != None):
			setting = Setting(key=name, value=value)
			db.session.add(setting)
	else:
		if (value == None):
			db.session.delete(setting)
		else:
			setting.value = value

def del_setting(name):
	return set_setting(name, None)


class Station(db.Model):
	stationID = db.Column(db.String(12), primary_key=True)
	channel = db.Column(db.Integer, index=True, unique=True)
	name = db.Column(db.String(128), index=True)
	callsign = db.Column(db.String(16))
	affiliate = db.Column(db.String(16))
	stationLogo = db.Column(db.String(512))
	enabled = db.Column(db.Boolean, default=False)
	hd = db.Column(db.Boolean)
	schedules = db.relationship('Schedule', back_populates='station', cascade="save-update, merge, delete, delete-orphan")
	airings = db.relationship('Airing', back_populates='station', cascade="save-update, merge, delete, delete-orphan")

	def __repr__(self):
		return 'Station<stationID: "{}", Channel: "{}", Name: "{}"">'.format(self.stationID, self.channel, self.name)


class Program(db.Model):
	programID = db.Column(db.String(14), primary_key=True)
	entityType = db.Column(db.String(32))
	title = db.Column(db.String(120))
	episodeTitle = db.Column(db.String(150))
	description = db.Column(db.String(100))
	longDescription = db.Column(db.String(1000))
	originalAirDate = db.Column(db.String(20))
	season_episode = db.Column(db.String(16))
	md5 = db.Column(db.String(22))
	airings = db.relationship('Airing', back_populates='program')

	def __repr__(self):
		return 'Program<programID: "{}", title: "{}", episodeTitle: "{}">'.format(self.programID, self.title, self.episodeTitle)


class Airing(db.Model):
	station = db.relationship('Station', back_populates='airings')
	stationID = db.Column(db.String(12), db.ForeignKey('station.stationID'), primary_key=True)
	program = db.relationship('Program', back_populates='airings')
	programID = db.Column(db.String(14), db.ForeignKey('program.programID'))
	airDateTime = db.Column(db.Integer, primary_key=True)
	duration = db.Column(db.Integer)
	new = db.Column(db.Boolean)
	md5 = db.Column(db.String(22))
	scheduled_recording = db.relationship('ScheduledRecording', back_populates='airings', uselist=False)
	recording_id = db.Column(db.String(14), db.ForeignKey('scheduled_recording.programID'))

	def __repr__(self):
		return 'Airing<stationID: "{}", programID: "{}", airDateTime: "{}">'.format(self.stationID, self.programID, self.airDateTime)


class Schedule(db.Model):
	station = db.relationship('Station', back_populates='schedules')
	stationID = db.Column(db.String(12), db.ForeignKey('station.stationID'), primary_key=True)
	date = db.Column(db.String(10), primary_key=True)
	lastModified = db.Column(db.Integer)
	md5 = db.Column(db.String(22))

	def __repr__(self):
		return 'Schedule<stationID: "{}", date: "{}", lastModified: "{}">'.format(self.stationID, self.date, self.lastModified)


class ScheduledRecording(db.Model):
	programID = db.Column(db.String(14), primary_key=True)
	series = db.Column(db.Boolean, default=False)
	title = db.Column(db.String(120))
	priority = db.Column(db.Integer, default=0)
	start_padding = db.Column(db.Integer, default=0)
	stop_padding = db.Column(db.Integer, default=0)
	prefer_station = db.relationship('Station')
	stationID = db.Column(db.String(12), db.ForeignKey('station.stationID'))
	any_station = db.Column(db.Boolean, default=False)
	new_only = db.Column(db.Boolean, default=False)
	airings = db.relationship('Airing', back_populates='scheduled_recording')

	def __repr__(self):
		return 'ScheduledRecording<programID: "{}", title: "{}">'.format(self.programID, self.title)


class RecordingJob(db.Model):
	program = db.relationship('Program')
	programID = db.Column(db.String(14), db.ForeignKey('program.programID'), primary_key=True)
	title = db.Column(db.String(120))
	episodeTitle = db.Column(db.String(150))
	season_episode = db.Column(db.String(16))
	channel = db.Column(db.Integer)
	filename = db.Column(db.String(1024))
	priority = db.Column(db.Integer, default=0)
	start_time = db.Column(db.Integer, default=0)
	duration = db.Column(db.Integer, default=0)
	start_padding = db.Column(db.Integer, default=0)
	stop_padding = db.Column(db.Integer, default=0)
	station = db.relationship('Station')
	stationID = db.Column(db.String(12), db.ForeignKey('station.stationID'))
	new = db.Column(db.Boolean, default=False)
	active = db.Column(db.Boolean, default=False)
	complete = db.Column(db.Boolean, default=False)

	def __repr__(self):
		return 'RecordingJob<programID: "{}", title: "{}", channel: "{}", start_time: "{}", duration: "{}">'.format(self.programID, self.title, self.channel, self.start_time, self.duration)
