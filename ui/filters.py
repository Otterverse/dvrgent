from ui import app
import datetime, time

@app.template_filter('int_to_datetime')
def format_datetime(value):
	return datetime.datetime.fromtimestamp(int(value)).strftime('%Y-%m-%d %H:%M:%S')
	
@app.template_filter('seconds_to_timecode')
def seconds_to_timecode(value):
	return time.strftime('%H:%M:%S', time.gmtime(value))