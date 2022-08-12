import requests, time, json, logging
from calendar import timegm


def sd_timestamp_to_unix(timestamp):
	try:
		return int(timegm(time.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")))
	except ValueError:
		return int(timegm(time.strptime(timestamp, "%Y-%m-%d")))


class AuthError(Exception):
	pass

class SchedulesDirect:

	def __init__(self, token=None):
		self.API_URL = 'https://json.schedulesdirect.org/20141201'
		self.userAgent = "python-schedulesdirect-0.0.1"
		self.token = token

	def api_login(self, username=None, password=None):

		if (username == None or password == None):
			raise Exception("No username/password provided for SchedulesDirect")

		headers = {'user-agent': self.userAgent}
		request_body = {"username": username, "password": password}
		r = requests.post(self.API_URL + "/token", json=request_body)
		data = r.json()
		if 'code' in data and 'message' in data:
			if data['code'] != 0:
				raise Exception("Unable to login: " + data['message'])
		else:
			raise Exception("Unable to login: " + data)
		r.raise_for_status()
		self.token = data['token']
		logging.debug("Token: " + self.token)
		return self.token

	def api_send(self, method, URI, payload=None):
		for x in range(0,1):
			try:		
				headers = {'user-agent': self.userAgent,'token': self.token}
				r = getattr(requests, method)(self.API_URL + URI, headers=headers, json=payload)
				r.raise_for_status()
				return r.json()
			except requests.exceptions.HTTPError as e:
				if(e.response.status_code == 403):
					raise AuthError("Authentication failure. Bad token? Did you login first?")
				else:
					raise e

	def api_status(self):
		data = self.api_send("get", "/status")
		status = {}
		status['lineup_code'] = data["lineups"][0]['lineup']
		status['lineup_modified'] = sd_timestamp_to_unix(data["lineups"][0]['modified'])
		status['system'] = data['systemStatus'][0]['status']
		status['systemMessage'] = data['systemStatus'][0]['message']
		status['accountMessage'] = ''
		try:
			status['accountMessage'] = data['account']['messages'][0]
		except:
			pass
		status['accountExpiration'] = sd_timestamp_to_unix(data['account']['expires'])

		return status

	def api_get_stations(self, lineup):
		return self.api_send("get", "/lineups/" + lineup)

	def api_get_schedule_md5s(self, station_list):
		return self.api_send("post", "/schedules/md5", payload=station_list)

	def api_get_schedules(self, schedule_request):
		return self.api_send("post", "/schedules", payload=schedule_request)

	def api_get_programs(self, program_list):
		return self.api_send("post", "/programs", payload=program_list)

