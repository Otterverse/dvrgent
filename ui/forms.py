from flask_wtf import Form
from wtforms import StringField, BooleanField, IntegerField, SubmitField, HiddenField

from wtforms_sqlalchemy.orm import model_form
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField

from ui.models import *


def enabled_stations():
	return Station.query.filter_by(enabled=True)

def get_id(obj):
	return obj.stationID


autoForm = model_form(ScheduledRecording, Form, exclude=['airings', 'prefer_station'])
class RecordForm(autoForm):
	prefer_station = QuerySelectField(query_factory=enabled_stations, get_label='name', get_pk=get_id)
	save = SubmitField("Save")
	fullID = HiddenField()


# class RecordForm(Form):
# 	programID = StringField("programID")
# 	series = BooleanField("Record Series?")
# 	new_only = BooleanField("New Only?")
# 	title = StringField("Title")
# 	priority = IntegerField("Priority")
# 	start_padding = IntegerField("Start Padding")
# 	stop_padding = IntegerField("Stop Padding")

# 	any_station = BooleanField("Any Station?")
# 	save = SubmitField("Save")
