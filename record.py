#!/usr/bin/python3

from libhdhomerun import *
import argparse, sys, time, os, signal





def status(device):
	hdhomerun_device_get_tuner_status(device, None, byref(tuner_status))
	print ('          channel:    %s' % (tuner_status.channel.decode('UTF-8').rstrip('\r\n')))
	print ('          lock:       %s' % (tuner_status.lock_str.decode('UTF-8').rstrip('\r\n')))
	print ('          present:    %i' % (tuner_status.signal_present))
	print ('          ss:         %i' % (tuner_status.signal_strength))
	print ('          snr:        %i' % (tuner_status.signal_to_noise_quality))
	print ('          seq:        %i' % (tuner_status.symbol_error_quality))
	print ('          bps:        %i' % (tuner_status.raw_bits_per_second))
	print ('          pps:        %i' % (tuner_status.packets_per_second))
	program = c_char_p()
	hdhomerun_device_get_tuner_program(device, byref(program))
	print ('          program:    %s' % (program.value.decode('UTF-8').rstrip('\r\n')))
	streaminfo = c_char_p()
	hdhomerun_device_get_tuner_streaminfo(device, byref(streaminfo))
	print ('          streaminfo: %s' % (streaminfo.value.decode('UTF-8').rstrip('\r\n').replace('\n', '; ')))
	filter = c_char_p()
	hdhomerun_device_get_tuner_filter(device, byref(filter))
	print ('          filter:     %s' % (filter.value.decode('UTF-8').rstrip('\r\n')))
	target = c_char_p()
	hdhomerun_device_get_tuner_target(device, byref(target))
	print ('          target:     %s' % (target.value.decode('UTF-8').rstrip('\r\n')))
	owner = c_char_p()
	hdhomerun_device_get_tuner_lockkey_owner(device, byref(owner))
	print ('          lock owner: %s' % (owner.value.decode('UTF-8').rstrip('\r\n')))
	tuner_vstatus = hdhomerun_tuner_vstatus_t()
	rc = hdhomerun_device_get_tuner_vstatus(device, None, byref(tuner_vstatus))
	print ('          vchannel:   %s' % (tuner_vstatus.vchannel.decode('UTF-8')))
	print ('          name:       %s' % (tuner_vstatus.name.decode('UTF-8')))
	print ('          auth:       %s' % (tuner_vstatus.auth.decode('UTF-8')))
	print ('          cgms:       %s' % (tuner_vstatus.cgms.decode('UTF-8')))
	print ('          not sub:    %i' % (tuner_vstatus.not_subscribed))
	print ('          not avail:  %i' % (tuner_vstatus.not_available))
	print ('          copy prot:  %i' % (tuner_vstatus.copy_protected))






#To parse hex
def auto_int(x):
    return int(x, 0)

#Get opts
parser = argparse.ArgumentParser(description='Record a TV channel to a file.')
parser.add_argument('channel', type=int, help='Channel number')
parser.add_argument('file', type=str, nargs='?', default='out.mpegts', help='Filename to write [out.mpegts]')
parser.add_argument('--duration', '-d', metavar='seconds', type=int, nargs='?', default='3600', help='Duration (in seconds) to record [3600]')
parser.add_argument('--device', type=auto_int, nargs='?', default=HDHOMERUN_DEVICE_ID_WILDCARD, help='DeviceID in hex [0x131E1B8A]')
parser.add_argument('--force', '-f', action='store_true', help='Overwrite existing file')
args = parser.parse_args()

#Open file
if (os.path.exists(args.file) and not args.force):
	print("File %s already exists! Use -f to clobber." % args.file)
	sys.exit()



#Our device list, one per tuner
device1 = hdhomerun_device_create(args.device, 0, 0, None)
#device2 = hdhomerun_device_create(args.device, 0, 1, None)
#device3 = hdhomerun_device_create(args.device, 0, 2, None)



#Free any existing locks. DANGER!
#hdhomerun_device_tuner_lockkey_release(device1)


#Get Lock
error = c_char_p()
if (hdhomerun_device_tuner_lockkey_request(device1, error) != 1):
	hdhomerun_device_destroy(device1)
	raise Exception("Could not get tuner lock: %s" % error.value.decode('UTF-8').rstrip('\r\n'))



#Tune channel and wait for signal lock
tuner_status = hdhomerun_tuner_status_t()
hdhomerun_device_set_tuner_vchannel(device1, str(args.channel).encode('utf-8'))
hdhomerun_device_wait_for_lock(device1, tuner_status)

status(device1)

#Set timers and interrupts
stop_record = False

def set_stop(signum, frame):
	global stop_record
	stop_record = True
	print("Finishing Recording")

old_alarm = signal.signal(signal.SIGALRM, set_stop)
old_int = signal.signal(signal.SIGINT, set_stop)

#Open file and record
with open(args.file, "wb") as file:
	signal.alarm(args.duration)
	print("Recording channel %i to %s for %i seconds." % (args.channel, args.file, args.duration))
	hdhomerun_device_stream_start(device1)
	while(stop_record == False):
		recv_size = c_size_t()
		data_ptr = hdhomerun_device_stream_recv(device1, VIDEO_DATA_BUFFER_SIZE_1S, recv_size)
		#print(recv_size.value)
		if(recv_size.value <= 0):
			time.sleep(0.025)
			#print("Underrun")
			continue
		data = string_at(data_ptr, size=recv_size.value)
		time.sleep(0.025)
		file.write(data)


signal.signal(signal.SIGALRM, old_alarm)
signal.signal(signal.SIGINT, old_int)


#Stop
hdhomerun_device_stream_stop(device1)

#Teardown
hdhomerun_device_tuner_lockkey_release(device1)
hdhomerun_device_destroy(device1)

