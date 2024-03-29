# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from jackal_msgs/Status.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import std_msgs.msg

class Status(genpy.Message):
  _md5sum = "c851ebcf9a6e20b196bc7894e285b4f6"
  _type = "jackal_msgs/Status"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# This message represents Jackal's lower-frequency status updates
# Default publish frequency is 1Hz.

Header header

# Commit of firmware source.
string hardware_id

# Times since MCU power-on and MCU rosserial connection, respectively.
duration mcu_uptime
duration connection_uptime

# Monitoring the run/stop loop. Changes in these values trigger an immediate
# publish, outside the ordinarily-scheduled 1Hz updates.
bool drivers_active
bool driver_external_stop_present
bool driver_external_stop_stopped

# Voltage rails, in volts
# Averaged over the message period
float32 measured_battery
float32 measured_12v
float32 measured_5v

# Current senses available on platform, in amps.
# Averaged over the message period
float32 drive_current
float32 user_current
float32 computer_current
float32 total_current

# Highest total system current peak as measured in a 1ms window.
float32 total_current_peak

# Integration of all power consumption since MCU power-on, in watt-hours.
float64 total_power_consumed 

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
  __slots__ = ['header','hardware_id','mcu_uptime','connection_uptime','drivers_active','driver_external_stop_present','driver_external_stop_stopped','measured_battery','measured_12v','measured_5v','drive_current','user_current','computer_current','total_current','total_current_peak','total_power_consumed']
  _slot_types = ['std_msgs/Header','string','duration','duration','bool','bool','bool','float32','float32','float32','float32','float32','float32','float32','float32','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,hardware_id,mcu_uptime,connection_uptime,drivers_active,driver_external_stop_present,driver_external_stop_stopped,measured_battery,measured_12v,measured_5v,drive_current,user_current,computer_current,total_current,total_current_peak,total_power_consumed

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Status, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.hardware_id is None:
        self.hardware_id = ''
      if self.mcu_uptime is None:
        self.mcu_uptime = genpy.Duration()
      if self.connection_uptime is None:
        self.connection_uptime = genpy.Duration()
      if self.drivers_active is None:
        self.drivers_active = False
      if self.driver_external_stop_present is None:
        self.driver_external_stop_present = False
      if self.driver_external_stop_stopped is None:
        self.driver_external_stop_stopped = False
      if self.measured_battery is None:
        self.measured_battery = 0.
      if self.measured_12v is None:
        self.measured_12v = 0.
      if self.measured_5v is None:
        self.measured_5v = 0.
      if self.drive_current is None:
        self.drive_current = 0.
      if self.user_current is None:
        self.user_current = 0.
      if self.computer_current is None:
        self.computer_current = 0.
      if self.total_current is None:
        self.total_current = 0.
      if self.total_current_peak is None:
        self.total_current_peak = 0.
      if self.total_power_consumed is None:
        self.total_power_consumed = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.hardware_id = ''
      self.mcu_uptime = genpy.Duration()
      self.connection_uptime = genpy.Duration()
      self.drivers_active = False
      self.driver_external_stop_present = False
      self.driver_external_stop_stopped = False
      self.measured_battery = 0.
      self.measured_12v = 0.
      self.measured_5v = 0.
      self.drive_current = 0.
      self.user_current = 0.
      self.computer_current = 0.
      self.total_current = 0.
      self.total_current_peak = 0.
      self.total_power_consumed = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.hardware_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_4i3B8fd().pack(_x.mcu_uptime.secs, _x.mcu_uptime.nsecs, _x.connection_uptime.secs, _x.connection_uptime.nsecs, _x.drivers_active, _x.driver_external_stop_present, _x.driver_external_stop_stopped, _x.measured_battery, _x.measured_12v, _x.measured_5v, _x.drive_current, _x.user_current, _x.computer_current, _x.total_current, _x.total_current_peak, _x.total_power_consumed))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.mcu_uptime is None:
        self.mcu_uptime = genpy.Duration()
      if self.connection_uptime is None:
        self.connection_uptime = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.hardware_id = str[start:end].decode('utf-8')
      else:
        self.hardware_id = str[start:end]
      _x = self
      start = end
      end += 59
      (_x.mcu_uptime.secs, _x.mcu_uptime.nsecs, _x.connection_uptime.secs, _x.connection_uptime.nsecs, _x.drivers_active, _x.driver_external_stop_present, _x.driver_external_stop_stopped, _x.measured_battery, _x.measured_12v, _x.measured_5v, _x.drive_current, _x.user_current, _x.computer_current, _x.total_current, _x.total_current_peak, _x.total_power_consumed,) = _get_struct_4i3B8fd().unpack(str[start:end])
      self.drivers_active = bool(self.drivers_active)
      self.driver_external_stop_present = bool(self.driver_external_stop_present)
      self.driver_external_stop_stopped = bool(self.driver_external_stop_stopped)
      self.mcu_uptime.canon()
      self.connection_uptime.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.hardware_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_4i3B8fd().pack(_x.mcu_uptime.secs, _x.mcu_uptime.nsecs, _x.connection_uptime.secs, _x.connection_uptime.nsecs, _x.drivers_active, _x.driver_external_stop_present, _x.driver_external_stop_stopped, _x.measured_battery, _x.measured_12v, _x.measured_5v, _x.drive_current, _x.user_current, _x.computer_current, _x.total_current, _x.total_current_peak, _x.total_power_consumed))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.mcu_uptime is None:
        self.mcu_uptime = genpy.Duration()
      if self.connection_uptime is None:
        self.connection_uptime = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.hardware_id = str[start:end].decode('utf-8')
      else:
        self.hardware_id = str[start:end]
      _x = self
      start = end
      end += 59
      (_x.mcu_uptime.secs, _x.mcu_uptime.nsecs, _x.connection_uptime.secs, _x.connection_uptime.nsecs, _x.drivers_active, _x.driver_external_stop_present, _x.driver_external_stop_stopped, _x.measured_battery, _x.measured_12v, _x.measured_5v, _x.drive_current, _x.user_current, _x.computer_current, _x.total_current, _x.total_current_peak, _x.total_power_consumed,) = _get_struct_4i3B8fd().unpack(str[start:end])
      self.drivers_active = bool(self.drivers_active)
      self.driver_external_stop_present = bool(self.driver_external_stop_present)
      self.driver_external_stop_stopped = bool(self.driver_external_stop_stopped)
      self.mcu_uptime.canon()
      self.connection_uptime.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_4i3B8fd = None
def _get_struct_4i3B8fd():
    global _struct_4i3B8fd
    if _struct_4i3B8fd is None:
        _struct_4i3B8fd = struct.Struct("<4i3B8fd")
    return _struct_4i3B8fd
