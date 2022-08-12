from hdhomerun.libhdhomerun import *
import ipaddress, os, time, threading, logging


class Tuner:

	def __init__(self, device_id=HDHOMERUN_DEVICE_ID_WILDCARD, device_ip=0, tuner_num=None):


		self._tuner_status = hdhomerun_tuner_status_t()

		self._status_time = time.time()

		if (tuner_num == None):
			discover_tuner = True
			tuner_num = 0
		else:
			discover_tuner = False
			if (tuner_num > 2 or tuner_num < 0):
				raise ValueError("tuner_num must be 0, 1, or 2.")

		self._device = hdhomerun_device_create(device_id, int(ipaddress.IPv4Address(device_ip)), tuner_num, None)

		if (self._device == None):
			raise Exception("Could not create tuner device.")

		try:
			if(self.model != 'hdhomerun3_cablecard'):
				raise Exception("Cannot contact device. Check Device ID and/or IP.")
		except:
			raise

		#Get Lock
		error = c_char_p()
		ret = -100
		if (discover_tuner == True):
			tuners = [0, 1, 2]
		else:
			tuners = [tuner_num]

		for tuner_num in tuners:
			logging.debug("Trying tuner number: %d" % tuner_num)
			hdhomerun_device_set_tuner(self._device, tuner_num)
			ret = hdhomerun_device_tuner_lockkey_request(self._device, error)
			if(ret == 1):
				break
		if (ret != 1):
			raise Exception("Could not get HW tuner lock: %s" % error.value.decode('UTF-8').rstrip('\r\n'))

		self.lock = threading.Lock()



	def __del__(self):
		try:
			logging.debug("Release HW lock for tuner")
			hdhomerun_device_tuner_lockkey_release(self._device)
			hdhomerun_device_destroy(self._device)
		except AttributeError:
			pass

	@property
	def device_id(self):
		return "%08X" % hdhomerun_device_get_device_id(self._device)

	@property
	def device_ip(self):
		return str(ipaddress.IPv4Address(hdhomerun_device_get_device_ip(self._device)))

	@property
	def tuner(self):
		return hdhomerun_device_get_tuner(self._device)

	@property
	def model(self):
		try:
			return hdhomerun_device_get_model_str(self._device).decode('UTF-8')
		except:
			return None

	#Only need to update status struct every half second at most
	def _get_status(self):
		if self._status_time < (time.time() - 0.5):
			self._status_time = time.time()
			hdhomerun_device_get_tuner_status(self._device, None, self._tuner_status)

	@property
	def ss(self):
		self._get_status()
		return self._tuner_status.signal_strength

	@property
	def snq(self):
		self._get_status()
		return self._tuner_status.signal_to_noise_quality

	@property
	def seq(self):
		self._get_status()
		return self._tuner_status.symbol_error_quality

	@property
	def bps(self):
		self._get_status()
		return self._tuner_status.raw_bits_per_second

	@property
	def pps(self):
		self._get_status()
		return self._tuner_status.packets_per_second

	@property
	def channel(self):
		channel_num = c_char_p()
		hdhomerun_device_get_tuner_vchannel(self._device, channel_num)
		return int(channel_num.value)

	@channel.setter
	def channel(self, channel_num):
		hdhomerun_device_set_tuner_vchannel(self._device, str(channel_num).encode('utf-8'))
		hdhomerun_device_wait_for_lock(self._device, self._tuner_status)

	def stream_start(self):
		hdhomerun_device_stream_start(self._device)

	def stream_stop(self):
		hdhomerun_device_stream_stop(self._device)

	def stream_recv(self):
		recv_size = c_size_t()
		data_ptr = hdhomerun_device_stream_recv(self._device, VIDEO_DATA_BUFFER_SIZE_1S, recv_size)
		if(recv_size.value <= 0):
			return None
		return string_at(data_ptr, size=recv_size.value)


class Recorder:
	def __init__(self, channel=None, filename=None, tuner=None, duration=False, delay=False):
		self.tuner = tuner
		#if(self.tuner == None):
		#	self.tuner = Tuner()

		self.should_run = False
		#self.channel = channel
		self._channel_num = channel
		self.filename = filename

		#if(os.path.exists(self.filename)):
		#	raise Exception("File %s Exists! Won't clobber." % self.filename)

		self.fp = open(filename, "wb")
		self.thread = threading.Thread(name='Recorder', target=self._run)

		logging.debug("Recorder setup: channel %i, filename '%s', duration %i, delay %i", channel, filename, duration, delay)

		if(duration):
			if(delay):
				self._start_time = time.time() + delay
			else:
				self._start_time = time.time()
			self._stop_time = self._start_time + duration
			self.start()


	def __del__(self):
		try:
			logging.debug("Recorder closing")
			self.fp.close()
			self.tuner.stream_stop()
			self.tuner.lock.release()
		except:
			pass


	@property
	def channel(self):
		return self.tuner.channel

	@channel.setter
	def channel(self, channel_num):
		self.tuner.channel = channel_num

	def start(self):
		if not self.thread.is_alive():
			self.should_run = True
			self.thread.start()
		else:
			logging.debug("Thread already started")

	def _run(self):
		logging.debug("Recorder Background Thread started")
		logging.debug(self._start_time)
		if self._start_time:
			logging.debug("Sleeping: %fs", self._start_time - time.time())
			while self._start_time > time.time():
				time.sleep(1)

		self.tuner = Tuner()
		self.channel = self._channel_num


		if self.tuner.lock.acquire(blocking=False):
			self.tuner.stream_start()
			while self.should_run:
				try:
					self.fp.write(self.tuner.stream_recv())
				except TypeError:
					pass
				time.sleep(0.025)
				try:
					if (time.time() > self._stop_time):
						self.should_run = False
				except AttributeError:
					pass

			self.tuner.stream_stop()
			self.tuner.lock.release()
		else:
			raise Exception("Could not acquire thread lock on tuner object!")

	def stop(self):
		self.should_run = False


class MultiRecorder:
	def __init__(self, channel=None, fp1=None, fp2=None):

		self.should_run = False
		self._channel = channel
		self.fp1 = fp1
		self.fp2 = fp2

		self.thread = threading.Thread(name='Recorder', target=self._run)

	def __del__(self):
		try:
			logging.debug("Recorder closing")
			self.fp1 = None
			self.fp2 = None
			self.tuner.stream_stop()
			self.tuner.lock.release()
		except:
			pass

	@property
	def channel(self):
		return self._channel

	@channel.setter
	def channel(self, channel_num):
		self._channel = channel_num
		if self.tuner:
			self.tuner.channel = channel_num

	def start(self):
		if self.thread.is_alive():
			logging.debug("Thread already started")
			return True
		else:
			self.tuner = Tuner()
			if self.tuner.lock.acquire(blocking=False):
				self.should_run = True
				self.thread.start()
				return True
			else:
				raise Exception("Could not acquire thread lock on tuner object!")

	def _run(self):
		logging.debug("Recorder Background Thread started")
		self.channel = self._channel

		logging.debug("Recording channel %i", self.channel)
		self.tuner.stream_start()
		while self.should_run:
			try:
				data = self.tuner.stream_recv()
				if self.fp1:
					self.fp1.write(data)
				if self.fp2:
					self.fp2.write(data)
			except TypeError:
				pass
			time.sleep(0.025)

		self.tuner.stream_stop()
		self.tuner.lock.release()

		self.fp1 = None
		self.fp2 = None



	def stop(self):
		self.should_run = False

	def add_file(self, fp):
		self.fp1 = self.fp2
		self.fp2 = fp

	def end_file(self):
		if self.fp1 == None:
			self.stop()
		else:
			self.fp1 = None
