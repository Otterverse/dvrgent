#import ctypes, os, sys
from ctypes import *

_libs = {}
_libs["hdhomerun"] = cdll.LoadLibrary("/usr/lib64/libhdhomerun.so")



# __off_t = c_long # /usr/include/bits/types.h: 140

# __off64_t = c_long # /usr/include/bits/types.h: 141

# # /usr/include/libio.h: 241
# class struct__IO_FILE(Structure):
#     pass

# FILE = struct__IO_FILE # /usr/include/bits/types/FILE.h: 7

# _IO_lock_t = None # /usr/include/libio.h: 150

# # /usr/include/libio.h: 156
# class struct__IO_marker(Structure):
#     pass

# struct__IO_marker.__slots__ = [
#     '_next',
#     '_sbuf',
#     '_pos',
# ]
# struct__IO_marker._fields_ = [
#     ('_next', POINTER(struct__IO_marker)),
#     ('_sbuf', POINTER(struct__IO_FILE)),
#     ('_pos', c_int),
# ]

# struct__IO_FILE.__slots__ = [
#     '_flags',
#     '_IO_read_ptr',
#     '_IO_read_end',
#     '_IO_read_base',
#     '_IO_write_base',
#     '_IO_write_ptr',
#     '_IO_write_end',
#     '_IO_buf_base',
#     '_IO_buf_end',
#     '_IO_save_base',
#     '_IO_backup_base',
#     '_IO_save_end',
#     '_markers',
#     '_chain',
#     '_fileno',
#     '_flags2',
#     '_old_offset',
#     '_cur_column',
#     '_vtable_offset',
#     '_shortbuf',
#     '_lock',
#     '_offset',
#     '__pad1',
#     '__pad2',
#     '__pad3',
#     '__pad4',
#     '__pad5',
#     '_mode',
#     '_unused2',
# ]
# struct__IO_FILE._fields_ = [
#     ('_flags', c_int),
#     ('_IO_read_ptr', c_char_p),
#     ('_IO_read_end', c_char_p),
#     ('_IO_read_base', c_char_p),
#     ('_IO_write_base', c_char_p),
#     ('_IO_write_ptr', c_char_p),
#     ('_IO_write_end', c_char_p),
#     ('_IO_buf_base', c_char_p),
#     ('_IO_buf_end', c_char_p),
#     ('_IO_save_base', c_char_p),
#     ('_IO_backup_base', c_char_p),
#     ('_IO_save_end', c_char_p),
#     ('_markers', POINTER(struct__IO_marker)),
#     ('_chain', POINTER(struct__IO_FILE)),
#     ('_fileno', c_int),
#     ('_flags2', c_int),
#     ('_old_offset', __off_t),
#     ('_cur_column', c_ushort),
#     ('_vtable_offset', c_char),
#     ('_shortbuf', c_char * 1),
#     ('_lock', POINTER(_IO_lock_t)),
#     ('_offset', __off64_t),
#     ('__pad1', POINTER(None)),
#     ('__pad2', POINTER(None)),
#     ('__pad3', POINTER(None)),
#     ('__pad4', POINTER(None)),
#     ('__pad5', c_size_t),
#     ('_mode', c_int),
#     ('_unused2', c_char * (((15 * sizeof(c_int)) - (4 * sizeof(POINTER(None)))) - sizeof(c_size_t))),
# ]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 68
class struct_hdhomerun_device_t(Structure):
    pass

# /home/user/source/libhdhomerun/hdhomerun_device.h: 68
class struct_hdhomerun_debug_t(Structure):
    pass

# /home/user/source/libhdhomerun/hdhomerun_device.h: 68
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_create'):
    hdhomerun_device_create = _libs['hdhomerun'].hdhomerun_device_create
    hdhomerun_device_create.restype = POINTER(struct_hdhomerun_device_t)
    hdhomerun_device_create.argtypes = [c_uint32, c_uint32, c_uint, POINTER(struct_hdhomerun_debug_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 69
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_create_multicast'):
    hdhomerun_device_create_multicast = _libs['hdhomerun'].hdhomerun_device_create_multicast
    hdhomerun_device_create_multicast.restype = POINTER(struct_hdhomerun_device_t)
    hdhomerun_device_create_multicast.argtypes = [c_uint32, c_uint16, POINTER(struct_hdhomerun_debug_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 70
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_create_from_str'):
    hdhomerun_device_create_from_str = _libs['hdhomerun'].hdhomerun_device_create_from_str
    hdhomerun_device_create_from_str.restype = POINTER(struct_hdhomerun_device_t)
    hdhomerun_device_create_from_str.argtypes = [c_char_p, POINTER(struct_hdhomerun_debug_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 71
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_destroy'):
    hdhomerun_device_destroy = _libs['hdhomerun'].hdhomerun_device_destroy
    hdhomerun_device_destroy.restype = None
    hdhomerun_device_destroy.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 76
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_name'):
    hdhomerun_device_get_name = _libs['hdhomerun'].hdhomerun_device_get_name
    hdhomerun_device_get_name.restype = c_char_p
    hdhomerun_device_get_name.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 77
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_device_id'):
    hdhomerun_device_get_device_id = _libs['hdhomerun'].hdhomerun_device_get_device_id
    hdhomerun_device_get_device_id.restype = c_uint32
    hdhomerun_device_get_device_id.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 78
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_device_ip'):
    hdhomerun_device_get_device_ip = _libs['hdhomerun'].hdhomerun_device_get_device_ip
    hdhomerun_device_get_device_ip.restype = c_uint32
    hdhomerun_device_get_device_ip.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 79
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_device_id_requested'):
    hdhomerun_device_get_device_id_requested = _libs['hdhomerun'].hdhomerun_device_get_device_id_requested
    hdhomerun_device_get_device_id_requested.restype = c_uint32
    hdhomerun_device_get_device_id_requested.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 80
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_device_ip_requested'):
    hdhomerun_device_get_device_ip_requested = _libs['hdhomerun'].hdhomerun_device_get_device_ip_requested
    hdhomerun_device_get_device_ip_requested.restype = c_uint32
    hdhomerun_device_get_device_ip_requested.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 81
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner'):
    hdhomerun_device_get_tuner = _libs['hdhomerun'].hdhomerun_device_get_tuner
    hdhomerun_device_get_tuner.restype = c_uint
    hdhomerun_device_get_tuner.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 83
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_device'):
    hdhomerun_device_set_device = _libs['hdhomerun'].hdhomerun_device_set_device
    hdhomerun_device_set_device.restype = c_int
    hdhomerun_device_set_device.argtypes = [POINTER(struct_hdhomerun_device_t), c_uint32, c_uint32]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 84
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_multicast'):
    hdhomerun_device_set_multicast = _libs['hdhomerun'].hdhomerun_device_set_multicast
    hdhomerun_device_set_multicast.restype = c_int
    hdhomerun_device_set_multicast.argtypes = [POINTER(struct_hdhomerun_device_t), c_uint32, c_uint16]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 85
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_tuner'):
    hdhomerun_device_set_tuner = _libs['hdhomerun'].hdhomerun_device_set_tuner
    hdhomerun_device_set_tuner.restype = c_int
    hdhomerun_device_set_tuner.argtypes = [POINTER(struct_hdhomerun_device_t), c_uint]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 86
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_tuner_from_str'):
    hdhomerun_device_set_tuner_from_str = _libs['hdhomerun'].hdhomerun_device_set_tuner_from_str
    hdhomerun_device_set_tuner_from_str.restype = c_int
    hdhomerun_device_set_tuner_from_str.argtypes = [POINTER(struct_hdhomerun_device_t), c_char_p]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 95
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_local_machine_addr'):
    hdhomerun_device_get_local_machine_addr = _libs['hdhomerun'].hdhomerun_device_get_local_machine_addr
    hdhomerun_device_get_local_machine_addr.restype = c_uint32
    hdhomerun_device_get_local_machine_addr.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_types.h: 29
class struct_hdhomerun_tuner_status_t(Structure):
    pass

# /home/user/source/libhdhomerun/hdhomerun_device.h: 108
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_status'):
    hdhomerun_device_get_tuner_status = _libs['hdhomerun'].hdhomerun_device_get_tuner_status
    hdhomerun_device_get_tuner_status.restype = c_int
    hdhomerun_device_get_tuner_status.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char), POINTER(struct_hdhomerun_tuner_status_t)]

# /home/user/source/libhdhomerun/hdhomerun_types.h: 42
class struct_hdhomerun_tuner_vstatus_t(Structure):
    pass

# /home/user/source/libhdhomerun/hdhomerun_device.h: 109
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_vstatus'):
    hdhomerun_device_get_tuner_vstatus = _libs['hdhomerun'].hdhomerun_device_get_tuner_vstatus
    hdhomerun_device_get_tuner_vstatus.restype = c_int
    hdhomerun_device_get_tuner_vstatus.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char), POINTER(struct_hdhomerun_tuner_vstatus_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 110
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_streaminfo'):
    hdhomerun_device_get_tuner_streaminfo = _libs['hdhomerun'].hdhomerun_device_get_tuner_streaminfo
    hdhomerun_device_get_tuner_streaminfo.restype = c_int
    hdhomerun_device_get_tuner_streaminfo.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char_p)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 111
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_channel'):
    hdhomerun_device_get_tuner_channel = _libs['hdhomerun'].hdhomerun_device_get_tuner_channel
    hdhomerun_device_get_tuner_channel.restype = c_int
    hdhomerun_device_get_tuner_channel.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char_p)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 112
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_vchannel'):
    hdhomerun_device_get_tuner_vchannel = _libs['hdhomerun'].hdhomerun_device_get_tuner_vchannel
    hdhomerun_device_get_tuner_vchannel.restype = c_int
    hdhomerun_device_get_tuner_vchannel.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char_p)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 113
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_channelmap'):
    hdhomerun_device_get_tuner_channelmap = _libs['hdhomerun'].hdhomerun_device_get_tuner_channelmap
    hdhomerun_device_get_tuner_channelmap.restype = c_int
    hdhomerun_device_get_tuner_channelmap.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char_p)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 114
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_filter'):
    hdhomerun_device_get_tuner_filter = _libs['hdhomerun'].hdhomerun_device_get_tuner_filter
    hdhomerun_device_get_tuner_filter.restype = c_int
    hdhomerun_device_get_tuner_filter.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char_p)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 115
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_program'):
    hdhomerun_device_get_tuner_program = _libs['hdhomerun'].hdhomerun_device_get_tuner_program
    hdhomerun_device_get_tuner_program.restype = c_int
    hdhomerun_device_get_tuner_program.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char_p)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 116
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_target'):
    hdhomerun_device_get_tuner_target = _libs['hdhomerun'].hdhomerun_device_get_tuner_target
    hdhomerun_device_get_tuner_target.restype = c_int
    hdhomerun_device_get_tuner_target.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char_p)]

# /home/user/source/libhdhomerun/hdhomerun_types.h: 77
class struct_hdhomerun_plotsample_t(Structure):
    pass

# /home/user/source/libhdhomerun/hdhomerun_device.h: 117
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_plotsample'):
    hdhomerun_device_get_tuner_plotsample = _libs['hdhomerun'].hdhomerun_device_get_tuner_plotsample
    hdhomerun_device_get_tuner_plotsample.restype = c_int
    hdhomerun_device_get_tuner_plotsample.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(struct_hdhomerun_plotsample_t), POINTER(c_size_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 118
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_lockkey_owner'):
    hdhomerun_device_get_tuner_lockkey_owner = _libs['hdhomerun'].hdhomerun_device_get_tuner_lockkey_owner
    hdhomerun_device_get_tuner_lockkey_owner.restype = c_int
    hdhomerun_device_get_tuner_lockkey_owner.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char_p)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 119
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_oob_status'):
    hdhomerun_device_get_oob_status = _libs['hdhomerun'].hdhomerun_device_get_oob_status
    hdhomerun_device_get_oob_status.restype = c_int
    hdhomerun_device_get_oob_status.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char_p), POINTER(struct_hdhomerun_tuner_status_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 120
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_oob_plotsample'):
    hdhomerun_device_get_oob_plotsample = _libs['hdhomerun'].hdhomerun_device_get_oob_plotsample
    hdhomerun_device_get_oob_plotsample.restype = c_int
    hdhomerun_device_get_oob_plotsample.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(struct_hdhomerun_plotsample_t), POINTER(c_size_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 121
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_ir_target'):
    hdhomerun_device_get_ir_target = _libs['hdhomerun'].hdhomerun_device_get_ir_target
    hdhomerun_device_get_ir_target.restype = c_int
    hdhomerun_device_get_ir_target.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char_p)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 122
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_version'):
    hdhomerun_device_get_version = _libs['hdhomerun'].hdhomerun_device_get_version
    hdhomerun_device_get_version.restype = c_int
    hdhomerun_device_get_version.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char_p), POINTER(c_uint32)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 123
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_supported'):
    hdhomerun_device_get_supported = _libs['hdhomerun'].hdhomerun_device_get_supported
    hdhomerun_device_get_supported.restype = c_int
    hdhomerun_device_get_supported.argtypes = [POINTER(struct_hdhomerun_device_t), c_char_p, POINTER(c_char_p)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 125
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_status_ss_color'):
    hdhomerun_device_get_tuner_status_ss_color = _libs['hdhomerun'].hdhomerun_device_get_tuner_status_ss_color
    hdhomerun_device_get_tuner_status_ss_color.restype = c_uint32
    hdhomerun_device_get_tuner_status_ss_color.argtypes = [POINTER(struct_hdhomerun_tuner_status_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 126
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_status_snq_color'):
    hdhomerun_device_get_tuner_status_snq_color = _libs['hdhomerun'].hdhomerun_device_get_tuner_status_snq_color
    hdhomerun_device_get_tuner_status_snq_color.restype = c_uint32
    hdhomerun_device_get_tuner_status_snq_color.argtypes = [POINTER(struct_hdhomerun_tuner_status_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 127
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_tuner_status_seq_color'):
    hdhomerun_device_get_tuner_status_seq_color = _libs['hdhomerun'].hdhomerun_device_get_tuner_status_seq_color
    hdhomerun_device_get_tuner_status_seq_color.restype = c_uint32
    hdhomerun_device_get_tuner_status_seq_color.argtypes = [POINTER(struct_hdhomerun_tuner_status_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 129
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_hw_model_str'):
    hdhomerun_device_get_hw_model_str = _libs['hdhomerun'].hdhomerun_device_get_hw_model_str
    hdhomerun_device_get_hw_model_str.restype = c_char_p
    hdhomerun_device_get_hw_model_str.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 130
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_model_str'):
    hdhomerun_device_get_model_str = _libs['hdhomerun'].hdhomerun_device_get_model_str
    hdhomerun_device_get_model_str.restype = c_char_p
    hdhomerun_device_get_model_str.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 141
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_tuner_channel'):
    hdhomerun_device_set_tuner_channel = _libs['hdhomerun'].hdhomerun_device_set_tuner_channel
    hdhomerun_device_set_tuner_channel.restype = c_int
    hdhomerun_device_set_tuner_channel.argtypes = [POINTER(struct_hdhomerun_device_t), c_char_p]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 142
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_tuner_vchannel'):
    hdhomerun_device_set_tuner_vchannel = _libs['hdhomerun'].hdhomerun_device_set_tuner_vchannel
    hdhomerun_device_set_tuner_vchannel.restype = c_int
    hdhomerun_device_set_tuner_vchannel.argtypes = [POINTER(struct_hdhomerun_device_t), c_char_p]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 143
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_tuner_channelmap'):
    hdhomerun_device_set_tuner_channelmap = _libs['hdhomerun'].hdhomerun_device_set_tuner_channelmap
    hdhomerun_device_set_tuner_channelmap.restype = c_int
    hdhomerun_device_set_tuner_channelmap.argtypes = [POINTER(struct_hdhomerun_device_t), c_char_p]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 144
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_tuner_filter'):
    hdhomerun_device_set_tuner_filter = _libs['hdhomerun'].hdhomerun_device_set_tuner_filter
    hdhomerun_device_set_tuner_filter.restype = c_int
    hdhomerun_device_set_tuner_filter.argtypes = [POINTER(struct_hdhomerun_device_t), c_char_p]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 145
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_tuner_filter_by_array'):
    hdhomerun_device_set_tuner_filter_by_array = _libs['hdhomerun'].hdhomerun_device_set_tuner_filter_by_array
    hdhomerun_device_set_tuner_filter_by_array.restype = c_int
    hdhomerun_device_set_tuner_filter_by_array.argtypes = [POINTER(struct_hdhomerun_device_t), c_ubyte * 8192]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 146
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_tuner_program'):
    hdhomerun_device_set_tuner_program = _libs['hdhomerun'].hdhomerun_device_set_tuner_program
    hdhomerun_device_set_tuner_program.restype = c_int
    hdhomerun_device_set_tuner_program.argtypes = [POINTER(struct_hdhomerun_device_t), c_char_p]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 147
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_tuner_target'):
    hdhomerun_device_set_tuner_target = _libs['hdhomerun'].hdhomerun_device_set_tuner_target
    hdhomerun_device_set_tuner_target.restype = c_int
    hdhomerun_device_set_tuner_target.argtypes = [POINTER(struct_hdhomerun_device_t), c_char_p]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 148
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_ir_target'):
    hdhomerun_device_set_ir_target = _libs['hdhomerun'].hdhomerun_device_set_ir_target
    hdhomerun_device_set_ir_target.restype = c_int
    hdhomerun_device_set_ir_target.argtypes = [POINTER(struct_hdhomerun_device_t), c_char_p]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 149
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_sys_dvbc_modulation'):
    hdhomerun_device_set_sys_dvbc_modulation = _libs['hdhomerun'].hdhomerun_device_set_sys_dvbc_modulation
    hdhomerun_device_set_sys_dvbc_modulation.restype = c_int
    hdhomerun_device_set_sys_dvbc_modulation.argtypes = [POINTER(struct_hdhomerun_device_t), c_char_p]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 168
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_var'):
    hdhomerun_device_get_var = _libs['hdhomerun'].hdhomerun_device_get_var
    hdhomerun_device_get_var.restype = c_int
    hdhomerun_device_get_var.argtypes = [POINTER(struct_hdhomerun_device_t), c_char_p, POINTER(c_char_p), POINTER(c_char_p)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 169
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_set_var'):
    hdhomerun_device_set_var = _libs['hdhomerun'].hdhomerun_device_set_var
    hdhomerun_device_set_var.restype = c_int
    hdhomerun_device_set_var.argtypes = [POINTER(struct_hdhomerun_device_t), c_char_p, c_char_p, POINTER(c_char_p), POINTER(c_char_p)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 184
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_tuner_lockkey_request'):
    hdhomerun_device_tuner_lockkey_request = _libs['hdhomerun'].hdhomerun_device_tuner_lockkey_request
    hdhomerun_device_tuner_lockkey_request.restype = c_int
    hdhomerun_device_tuner_lockkey_request.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(c_char_p)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 185
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_tuner_lockkey_release'):
    hdhomerun_device_tuner_lockkey_release = _libs['hdhomerun'].hdhomerun_device_tuner_lockkey_release
    hdhomerun_device_tuner_lockkey_release.restype = c_int
    hdhomerun_device_tuner_lockkey_release.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 186
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_tuner_lockkey_force'):
    hdhomerun_device_tuner_lockkey_force = _libs['hdhomerun'].hdhomerun_device_tuner_lockkey_force
    hdhomerun_device_tuner_lockkey_force.restype = c_int
    hdhomerun_device_tuner_lockkey_force.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 191
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_tuner_lockkey_use_value'):
    hdhomerun_device_tuner_lockkey_use_value = _libs['hdhomerun'].hdhomerun_device_tuner_lockkey_use_value
    hdhomerun_device_tuner_lockkey_use_value.restype = None
    hdhomerun_device_tuner_lockkey_use_value.argtypes = [POINTER(struct_hdhomerun_device_t), c_uint32]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 203
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_wait_for_lock'):
    hdhomerun_device_wait_for_lock = _libs['hdhomerun'].hdhomerun_device_wait_for_lock
    hdhomerun_device_wait_for_lock.restype = c_int
    hdhomerun_device_wait_for_lock.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(struct_hdhomerun_tuner_status_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 221
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_stream_start'):
    hdhomerun_device_stream_start = _libs['hdhomerun'].hdhomerun_device_stream_start
    hdhomerun_device_stream_start.restype = c_int
    hdhomerun_device_stream_start.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 222
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_stream_recv'):
    hdhomerun_device_stream_recv = _libs['hdhomerun'].hdhomerun_device_stream_recv
    hdhomerun_device_stream_recv.restype = POINTER(c_uint8)
    hdhomerun_device_stream_recv.argtypes = [POINTER(struct_hdhomerun_device_t), c_size_t, POINTER(c_size_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 223
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_stream_flush'):
    hdhomerun_device_stream_flush = _libs['hdhomerun'].hdhomerun_device_stream_flush
    hdhomerun_device_stream_flush.restype = None
    hdhomerun_device_stream_flush.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 224
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_stream_stop'):
    hdhomerun_device_stream_stop = _libs['hdhomerun'].hdhomerun_device_stream_stop
    hdhomerun_device_stream_stop.restype = None
    hdhomerun_device_stream_stop.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 229
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_channelscan_init'):
    hdhomerun_device_channelscan_init = _libs['hdhomerun'].hdhomerun_device_channelscan_init
    hdhomerun_device_channelscan_init.restype = c_int
    hdhomerun_device_channelscan_init.argtypes = [POINTER(struct_hdhomerun_device_t), c_char_p]

# /home/user/source/libhdhomerun/hdhomerun_types.h: 64
class struct_hdhomerun_channelscan_result_t(Structure):
    pass

# /home/user/source/libhdhomerun/hdhomerun_device.h: 230
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_channelscan_advance'):
    hdhomerun_device_channelscan_advance = _libs['hdhomerun'].hdhomerun_device_channelscan_advance
    hdhomerun_device_channelscan_advance.restype = c_int
    hdhomerun_device_channelscan_advance.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(struct_hdhomerun_channelscan_result_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 231
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_channelscan_detect'):
    hdhomerun_device_channelscan_detect = _libs['hdhomerun'].hdhomerun_device_channelscan_detect
    hdhomerun_device_channelscan_detect.restype = c_int
    hdhomerun_device_channelscan_detect.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(struct_hdhomerun_channelscan_result_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 232
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_channelscan_get_progress'):
    hdhomerun_device_channelscan_get_progress = _libs['hdhomerun'].hdhomerun_device_channelscan_get_progress
    hdhomerun_device_channelscan_get_progress.restype = c_uint8
    hdhomerun_device_channelscan_get_progress.argtypes = [POINTER(struct_hdhomerun_device_t)]

# # /home/user/source/libhdhomerun/hdhomerun_device.h: 243
# if hasattr(_libs['hdhomerun'], 'hdhomerun_device_upgrade'):
#     hdhomerun_device_upgrade = _libs['hdhomerun'].hdhomerun_device_upgrade
#     hdhomerun_device_upgrade.restype = c_int
#     hdhomerun_device_upgrade.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(FILE)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 248
class struct_hdhomerun_control_sock_t(Structure):
    pass

# /home/user/source/libhdhomerun/hdhomerun_device.h: 248
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_control_sock'):
    hdhomerun_device_get_control_sock = _libs['hdhomerun'].hdhomerun_device_get_control_sock
    hdhomerun_device_get_control_sock.restype = POINTER(struct_hdhomerun_control_sock_t)
    hdhomerun_device_get_control_sock.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 249
class struct_hdhomerun_video_sock_t(Structure):
    pass

# /home/user/source/libhdhomerun/hdhomerun_device.h: 249
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_video_sock'):
    hdhomerun_device_get_video_sock = _libs['hdhomerun'].hdhomerun_device_get_video_sock
    hdhomerun_device_get_video_sock.restype = POINTER(struct_hdhomerun_video_sock_t)
    hdhomerun_device_get_video_sock.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 254
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_debug_print_video_stats'):
    hdhomerun_device_debug_print_video_stats = _libs['hdhomerun'].hdhomerun_device_debug_print_video_stats
    hdhomerun_device_debug_print_video_stats.restype = None
    hdhomerun_device_debug_print_video_stats.argtypes = [POINTER(struct_hdhomerun_device_t)]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 255
class struct_hdhomerun_video_stats_t(Structure):
    pass

# /home/user/source/libhdhomerun/hdhomerun_device.h: 255
if hasattr(_libs['hdhomerun'], 'hdhomerun_device_get_video_stats'):
    hdhomerun_device_get_video_stats = _libs['hdhomerun'].hdhomerun_device_get_video_stats
    hdhomerun_device_get_video_stats.restype = None
    hdhomerun_device_get_video_stats.argtypes = [POINTER(struct_hdhomerun_device_t), POINTER(struct_hdhomerun_video_stats_t)]

# /home/user/source/libhdhomerun/hdhomerun_discover.h: 28
class struct_hdhomerun_discover_device_t(Structure):
    pass

struct_hdhomerun_discover_device_t.__slots__ = [
    'ip_addr',
    'device_type',
    'device_id',
    'tuner_count',
    'is_legacy',
    'device_auth',
    'base_url',
]
struct_hdhomerun_discover_device_t._fields_ = [
    ('ip_addr', c_uint32),
    ('device_type', c_uint32),
    ('device_id', c_uint32),
    ('tuner_count', c_uint8),
    ('is_legacy', c_uint8),
    ('device_auth', c_char * 25),
    ('base_url', c_char * 29),
]

# /home/user/source/libhdhomerun/hdhomerun_discover.h: 52
if hasattr(_libs['hdhomerun'], 'hdhomerun_discover_find_devices_custom_v2'):
    hdhomerun_discover_find_devices_custom_v2 = _libs['hdhomerun'].hdhomerun_discover_find_devices_custom_v2
    hdhomerun_discover_find_devices_custom_v2.restype = c_int
    hdhomerun_discover_find_devices_custom_v2.argtypes = [c_uint32, c_uint32, c_uint32, POINTER(struct_hdhomerun_discover_device_t), c_int]

# /home/user/source/libhdhomerun/hdhomerun_discover.h: 57
class struct_hdhomerun_discover_t(Structure):
    pass

# /home/user/source/libhdhomerun/hdhomerun_discover.h: 57
if hasattr(_libs['hdhomerun'], 'hdhomerun_discover_create'):
    hdhomerun_discover_create = _libs['hdhomerun'].hdhomerun_discover_create
    hdhomerun_discover_create.restype = POINTER(struct_hdhomerun_discover_t)
    hdhomerun_discover_create.argtypes = [POINTER(struct_hdhomerun_debug_t)]

# /home/user/source/libhdhomerun/hdhomerun_discover.h: 58
if hasattr(_libs['hdhomerun'], 'hdhomerun_discover_destroy'):
    hdhomerun_discover_destroy = _libs['hdhomerun'].hdhomerun_discover_destroy
    hdhomerun_discover_destroy.restype = None
    hdhomerun_discover_destroy.argtypes = [POINTER(struct_hdhomerun_discover_t)]

# /home/user/source/libhdhomerun/hdhomerun_discover.h: 59
if hasattr(_libs['hdhomerun'], 'hdhomerun_discover_find_devices_v2'):
    hdhomerun_discover_find_devices_v2 = _libs['hdhomerun'].hdhomerun_discover_find_devices_v2
    hdhomerun_discover_find_devices_v2.restype = c_int
    hdhomerun_discover_find_devices_v2.argtypes = [POINTER(struct_hdhomerun_discover_t), c_uint32, c_uint32, c_uint32, POINTER(struct_hdhomerun_discover_device_t), c_int]

# /home/user/source/libhdhomerun/hdhomerun_discover.h: 70
if hasattr(_libs['hdhomerun'], 'hdhomerun_discover_validate_device_id'):
    hdhomerun_discover_validate_device_id = _libs['hdhomerun'].hdhomerun_discover_validate_device_id
    hdhomerun_discover_validate_device_id.restype = c_uint8
    hdhomerun_discover_validate_device_id.argtypes = [c_uint32]

# /home/user/source/libhdhomerun/hdhomerun_discover.h: 78
if hasattr(_libs['hdhomerun'], 'hdhomerun_discover_is_ip_multicast'):
    hdhomerun_discover_is_ip_multicast = _libs['hdhomerun'].hdhomerun_discover_is_ip_multicast
    hdhomerun_discover_is_ip_multicast.restype = c_uint8
    hdhomerun_discover_is_ip_multicast.argtypes = [c_uint32]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 145
# class struct_hdhomerun_pkt_t(Structure):
#     pass

# struct_hdhomerun_pkt_t.__slots__ = [
#     'pos',
#     'start',
#     'end',
#     'limit',
#     'buffer',
# ]
# struct_hdhomerun_pkt_t._fields_ = [
#     ('pos', POINTER(c_uint8)),
#     ('start', POINTER(c_uint8)),
#     ('end', POINTER(c_uint8)),
#     ('limit', POINTER(c_uint8)),
#     ('buffer', c_uint8 * 3074),
# ]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 153
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_create'):
#     hdhomerun_pkt_create = _libs['hdhomerun'].hdhomerun_pkt_create
#     hdhomerun_pkt_create.restype = POINTER(struct_hdhomerun_pkt_t)
#     hdhomerun_pkt_create.argtypes = []

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 154
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_destroy'):
#     hdhomerun_pkt_destroy = _libs['hdhomerun'].hdhomerun_pkt_destroy
#     hdhomerun_pkt_destroy.restype = None
#     hdhomerun_pkt_destroy.argtypes = [POINTER(struct_hdhomerun_pkt_t)]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 155
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_reset'):
#     hdhomerun_pkt_reset = _libs['hdhomerun'].hdhomerun_pkt_reset
#     hdhomerun_pkt_reset.restype = None
#     hdhomerun_pkt_reset.argtypes = [POINTER(struct_hdhomerun_pkt_t)]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 157
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_read_u8'):
#     hdhomerun_pkt_read_u8 = _libs['hdhomerun'].hdhomerun_pkt_read_u8
#     hdhomerun_pkt_read_u8.restype = c_uint8
#     hdhomerun_pkt_read_u8.argtypes = [POINTER(struct_hdhomerun_pkt_t)]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 158
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_read_u16'):
#     hdhomerun_pkt_read_u16 = _libs['hdhomerun'].hdhomerun_pkt_read_u16
#     hdhomerun_pkt_read_u16.restype = c_uint16
#     hdhomerun_pkt_read_u16.argtypes = [POINTER(struct_hdhomerun_pkt_t)]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 159
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_read_u32'):
#     hdhomerun_pkt_read_u32 = _libs['hdhomerun'].hdhomerun_pkt_read_u32
#     hdhomerun_pkt_read_u32.restype = c_uint32
#     hdhomerun_pkt_read_u32.argtypes = [POINTER(struct_hdhomerun_pkt_t)]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 160
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_read_var_length'):
#     hdhomerun_pkt_read_var_length = _libs['hdhomerun'].hdhomerun_pkt_read_var_length
#     hdhomerun_pkt_read_var_length.restype = c_size_t
#     hdhomerun_pkt_read_var_length.argtypes = [POINTER(struct_hdhomerun_pkt_t)]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 161
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_read_tlv'):
#     hdhomerun_pkt_read_tlv = _libs['hdhomerun'].hdhomerun_pkt_read_tlv
#     hdhomerun_pkt_read_tlv.restype = POINTER(c_uint8)
#     hdhomerun_pkt_read_tlv.argtypes = [POINTER(struct_hdhomerun_pkt_t), POINTER(c_uint8), POINTER(c_size_t)]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 162
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_read_mem'):
#     hdhomerun_pkt_read_mem = _libs['hdhomerun'].hdhomerun_pkt_read_mem
#     hdhomerun_pkt_read_mem.restype = None
#     hdhomerun_pkt_read_mem.argtypes = [POINTER(struct_hdhomerun_pkt_t), POINTER(None), c_size_t]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 164
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_write_u8'):
#     hdhomerun_pkt_write_u8 = _libs['hdhomerun'].hdhomerun_pkt_write_u8
#     hdhomerun_pkt_write_u8.restype = None
#     hdhomerun_pkt_write_u8.argtypes = [POINTER(struct_hdhomerun_pkt_t), c_uint8]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 165
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_write_u16'):
#     hdhomerun_pkt_write_u16 = _libs['hdhomerun'].hdhomerun_pkt_write_u16
#     hdhomerun_pkt_write_u16.restype = None
#     hdhomerun_pkt_write_u16.argtypes = [POINTER(struct_hdhomerun_pkt_t), c_uint16]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 166
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_write_u32'):
#     hdhomerun_pkt_write_u32 = _libs['hdhomerun'].hdhomerun_pkt_write_u32
#     hdhomerun_pkt_write_u32.restype = None
#     hdhomerun_pkt_write_u32.argtypes = [POINTER(struct_hdhomerun_pkt_t), c_uint32]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 167
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_write_var_length'):
#     hdhomerun_pkt_write_var_length = _libs['hdhomerun'].hdhomerun_pkt_write_var_length
#     hdhomerun_pkt_write_var_length.restype = None
#     hdhomerun_pkt_write_var_length.argtypes = [POINTER(struct_hdhomerun_pkt_t), c_size_t]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 168
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_write_mem'):
#     hdhomerun_pkt_write_mem = _libs['hdhomerun'].hdhomerun_pkt_write_mem
#     hdhomerun_pkt_write_mem.restype = None
#     hdhomerun_pkt_write_mem.argtypes = [POINTER(struct_hdhomerun_pkt_t), POINTER(None), c_size_t]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 170
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_open_frame'):
#     hdhomerun_pkt_open_frame = _libs['hdhomerun'].hdhomerun_pkt_open_frame
#     hdhomerun_pkt_open_frame.restype = c_int
#     hdhomerun_pkt_open_frame.argtypes = [POINTER(struct_hdhomerun_pkt_t), POINTER(c_uint16)]

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 171
# if hasattr(_libs['hdhomerun'], 'hdhomerun_pkt_seal_frame'):
#     hdhomerun_pkt_seal_frame = _libs['hdhomerun'].hdhomerun_pkt_seal_frame
#     hdhomerun_pkt_seal_frame.restype = None
#     hdhomerun_pkt_seal_frame.argtypes = [POINTER(struct_hdhomerun_pkt_t), c_uint16]

# /home/user/source/libhdhomerun/hdhomerun_types.h: 27
class struct_hdhomerun_device_allocation_t(Structure):
    pass

struct_hdhomerun_tuner_status_t.__slots__ = [
    'channel',
    'lock_str',
    'signal_present',
    'lock_supported',
    'lock_unsupported',
    'signal_strength',
    'signal_to_noise_quality',
    'symbol_error_quality',
    'raw_bits_per_second',
    'packets_per_second',
]
struct_hdhomerun_tuner_status_t._fields_ = [
    ('channel', c_char * 32),
    ('lock_str', c_char * 32),
    ('signal_present', c_uint8),
    ('lock_supported', c_uint8),
    ('lock_unsupported', c_uint8),
    ('signal_strength', c_uint),
    ('signal_to_noise_quality', c_uint),
    ('symbol_error_quality', c_uint),
    ('raw_bits_per_second', c_uint32),
    ('packets_per_second', c_uint32),
]

struct_hdhomerun_tuner_vstatus_t.__slots__ = [
    'vchannel',
    'name',
    'auth',
    'cci',
    'cgms',
    'not_subscribed',
    'not_available',
    'copy_protected',
]
struct_hdhomerun_tuner_vstatus_t._fields_ = [
    ('vchannel', c_char * 32),
    ('name', c_char * 32),
    ('auth', c_char * 32),
    ('cci', c_char * 32),
    ('cgms', c_char * 32),
    ('not_subscribed', c_uint8),
    ('not_available', c_uint8),
    ('copy_protected', c_uint8),
]

# /home/user/source/libhdhomerun/hdhomerun_types.h: 53
class struct_hdhomerun_channelscan_program_t(Structure):
    pass

struct_hdhomerun_channelscan_program_t.__slots__ = [
    'program_str',
    'program_number',
    'virtual_major',
    'virtual_minor',
    'type',
    'name',
]
struct_hdhomerun_channelscan_program_t._fields_ = [
    ('program_str', c_char * 64),
    ('program_number', c_uint16),
    ('virtual_major', c_uint16),
    ('virtual_minor', c_uint16),
    ('type', c_uint16),
    ('name', c_char * 32),
]

struct_hdhomerun_channelscan_result_t.__slots__ = [
    'channel_str',
    'channelmap',
    'frequency',
    'status',
    'program_count',
    'programs',
    'transport_stream_id_detected',
    'original_network_id_detected',
    'transport_stream_id',
    'original_network_id',
]
struct_hdhomerun_channelscan_result_t._fields_ = [
    ('channel_str', c_char * 64),
    ('channelmap', c_uint32),
    ('frequency', c_uint32),
    ('status', struct_hdhomerun_tuner_status_t),
    ('program_count', c_int),
    ('programs', struct_hdhomerun_channelscan_program_t * 64),
    ('transport_stream_id_detected', c_uint8),
    ('original_network_id_detected', c_uint8),
    ('transport_stream_id', c_uint16),
    ('original_network_id', c_uint16),
]

struct_hdhomerun_plotsample_t.__slots__ = [
    'real',
    'imag',
]
struct_hdhomerun_plotsample_t._fields_ = [
    ('real', c_int16),
    ('imag', c_int16),
]

# /home/user/source/libhdhomerun/hdhomerun_device.h: 26
try:
    HDHOMERUN_DEVICE_MAX_TUNE_TO_LOCK_TIME = 1500
except:
    pass

# /home/user/source/libhdhomerun/hdhomerun_device.h: 26
try:
    HDHOMERUN_DEVICE_MAX_LOCK_TO_DATA_TIME = 2000
except:
    pass

# /home/user/source/libhdhomerun/hdhomerun_device.h: 26
try:
    HDHOMERUN_DEVICE_MAX_TUNE_TO_DATA_TIME = (HDHOMERUN_DEVICE_MAX_TUNE_TO_LOCK_TIME + HDHOMERUN_DEVICE_MAX_LOCK_TO_DATA_TIME)
except:
    pass

# /home/user/source/libhdhomerun/hdhomerun_device.h: 27
try:
    HDHOMERUN_TARGET_PROTOCOL_UDP = 'udp'
except:
    pass

# /home/user/source/libhdhomerun/hdhomerun_device.h: 27
try:
    HDHOMERUN_TARGET_PROTOCOL_RTP = 'rtp'
except:
    pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 114
# try:
#     HDHOMERUN_DISCOVER_UDP_PORT = 65001
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 114
# try:
#     HDHOMERUN_CONTROL_TCP_PORT = 65001
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 115
# try:
#     HDHOMERUN_MAX_PACKET_SIZE = 1460
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 115
# try:
#     HDHOMERUN_MAX_PAYLOAD_SIZE = 1452
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 116
# try:
#     HDHOMERUN_TYPE_DISCOVER_REQ = 2
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 116
# try:
#     HDHOMERUN_TYPE_DISCOVER_RPY = 3
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 116
# try:
#     HDHOMERUN_TYPE_GETSET_REQ = 4
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 116
# try:
#     HDHOMERUN_TYPE_GETSET_RPY = 5
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 116
# try:
#     HDHOMERUN_TYPE_UPGRADE_REQ = 6
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 116
# try:
#     HDHOMERUN_TYPE_UPGRADE_RPY = 7
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 117
# try:
#     HDHOMERUN_TAG_DEVICE_TYPE = 1
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 117
# try:
#     HDHOMERUN_TAG_DEVICE_ID = 2
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 117
# try:
#     HDHOMERUN_TAG_GETSET_NAME = 3
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 117
# try:
#     HDHOMERUN_TAG_GETSET_VALUE = 4
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 117
# try:
#     HDHOMERUN_TAG_GETSET_LOCKKEY = 21
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 117
# try:
#     HDHOMERUN_TAG_ERROR_MESSAGE = 5
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 117
# try:
#     HDHOMERUN_TAG_TUNER_COUNT = 16
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 117
# try:
#     HDHOMERUN_TAG_DEVICE_AUTH_BIN = 41
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 117
# try:
#     HDHOMERUN_TAG_BASE_URL = 42
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 117
# try:
#     HDHOMERUN_TAG_DEVICE_AUTH_STR = 43
# except:
#     pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 118
# try:
#     HDHOMERUN_DEVICE_TYPE_WILDCARD = 4294967295
# except:
#     pass

# /home/user/source/libhdhomerun/hdhomerun_pkt.h: 118
try:
    HDHOMERUN_DEVICE_TYPE_TUNER = 1
except:
    pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 118
# try:
#     HDHOMERUN_DEVICE_TYPE_STORAGE = 5
# except:
#     pass

# /home/user/source/libhdhomerun/hdhomerun_pkt.h: 118
try:
    HDHOMERUN_DEVICE_ID_WILDCARD = 4294967295
except:
    pass

# # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 119
# try:
#     HDHOMERUN_MIN_PEEK_LENGTH = 4
# except:
#     pass

# /home/user/source/libhdhomerun/hdhomerun_types.h: 21
try:
    HDHOMERUN_STATUS_COLOR_NEUTRAL = 4294967295
except:
    pass

# /home/user/source/libhdhomerun/hdhomerun_types.h: 21
try:
    HDHOMERUN_STATUS_COLOR_RED = 4294901760
except:
    pass

# /home/user/source/libhdhomerun/hdhomerun_types.h: 21
try:
    HDHOMERUN_STATUS_COLOR_YELLOW = 4294967040
except:
    pass

# /home/user/source/libhdhomerun/hdhomerun_types.h: 21
try:
    HDHOMERUN_STATUS_COLOR_GREEN = 4278239232
except:
    pass

# /home/user/source/libhdhomerun/hdhomerun_types.h: 58
try:
    HDHOMERUN_CHANNELSCAN_MAX_PROGRAM_COUNT = 64
except:
    pass

hdhomerun_device_t = struct_hdhomerun_device_t # /home/user/source/libhdhomerun/hdhomerun_device.h: 68

hdhomerun_debug_t = struct_hdhomerun_debug_t # /home/user/source/libhdhomerun/hdhomerun_device.h: 68

hdhomerun_tuner_status_t = struct_hdhomerun_tuner_status_t # /home/user/source/libhdhomerun/hdhomerun_types.h: 29

hdhomerun_tuner_vstatus_t = struct_hdhomerun_tuner_vstatus_t # /home/user/source/libhdhomerun/hdhomerun_types.h: 42

hdhomerun_plotsample_t = struct_hdhomerun_plotsample_t # /home/user/source/libhdhomerun/hdhomerun_types.h: 77

hdhomerun_channelscan_result_t = struct_hdhomerun_channelscan_result_t # /home/user/source/libhdhomerun/hdhomerun_types.h: 64

hdhomerun_control_sock_t = struct_hdhomerun_control_sock_t # /home/user/source/libhdhomerun/hdhomerun_device.h: 248

hdhomerun_video_sock_t = struct_hdhomerun_video_sock_t # /home/user/source/libhdhomerun/hdhomerun_device.h: 249

hdhomerun_video_stats_t = struct_hdhomerun_video_stats_t # /home/user/source/libhdhomerun/hdhomerun_device.h: 255

hdhomerun_discover_device_t = struct_hdhomerun_discover_device_t # /home/user/source/libhdhomerun/hdhomerun_discover.h: 28

hdhomerun_discover_t = struct_hdhomerun_discover_t # /home/user/source/libhdhomerun/hdhomerun_discover.h: 57

# hdhomerun_pkt_t = struct_hdhomerun_pkt_t # /home/user/source/libhdhomerun/hdhomerun_pkt.h: 145

hdhomerun_device_allocation_t = struct_hdhomerun_device_allocation_t # /home/user/source/libhdhomerun/hdhomerun_types.h: 27

hdhomerun_channelscan_program_t = struct_hdhomerun_channelscan_program_t # /home/user/source/libhdhomerun/hdhomerun_types.h: 53


VIDEO_DATA_BUFFER_SIZE_1S = c_size_t(int(20000000 / 8))