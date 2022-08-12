#!/usr/bin/python3
from ui import app, db, schedules
from ui.models import get_setting, set_setting
import hashlib

#Setup new DB and basic settings
db.create_all()
if (not get_setting('username') or not get_setting('password') or not get_setting('lineup')):
	set_setting('username', input('SD Username: '))
	set_setting('password', hashlib.sha1(input("SD Password: ").encode('UTF-8')).hexdigest())
	set_setting('lineup', input('SD Lineup [USA-XXXXXXX-X]: '))
	set_setting('save_path', input('Storage Location [/tmp]: ') or "/tmp")
	print(get_setting('password'))

schedules.fetch_updates()

