# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensormanager/sensormanager.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensormanager/sensormanager.proto',
  package='sensormanager',
  syntax='proto3',
  serialized_options=_b('\n\036io.grpc.examples.sensormanagerB\rSensorManagerP\001\242\002\003HLW'),
  serialized_pb=_b('\n!sensormanager/sensormanager.proto\x12\rsensormanager\"-\n\x19\x41llSensorsOnVesselRequest\x12\x10\n\x08vesselID\x18\x01 \x01(\t\"D\n\x1a\x41llSensorsOnVesselResponse\x12&\n\x07sensors\x18\x01 \x03(\x0b\x32\x15.sensormanager.Sensor\"A\n\x06Sensor\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x13\n\x0bsensorWidth\x18\x02 \x01(\x05\x12\x14\n\x0csensorHeight\x18\x03 \x01(\x05\x32\x7f\n\rSensorManager\x12n\n\x15GetAllSensorsOnVessel\x12(.sensormanager.AllSensorsOnVesselRequest\x1a).sensormanager.AllSensorsOnVesselResponse\"\x00\x42\x37\n\x1eio.grpc.examples.sensormanagerB\rSensorManagerP\x01\xa2\x02\x03HLWb\x06proto3')
)




_ALLSENSORSONVESSELREQUEST = _descriptor.Descriptor(
  name='AllSensorsOnVesselRequest',
  full_name='sensormanager.AllSensorsOnVesselRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vesselID', full_name='sensormanager.AllSensorsOnVesselRequest.vesselID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=97,
)


_ALLSENSORSONVESSELRESPONSE = _descriptor.Descriptor(
  name='AllSensorsOnVesselResponse',
  full_name='sensormanager.AllSensorsOnVesselResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensors', full_name='sensormanager.AllSensorsOnVesselResponse.sensors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=167,
)


_SENSOR = _descriptor.Descriptor(
  name='Sensor',
  full_name='sensormanager.Sensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sensormanager.Sensor.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensorWidth', full_name='sensormanager.Sensor.sensorWidth', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensorHeight', full_name='sensormanager.Sensor.sensorHeight', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=234,
)

_ALLSENSORSONVESSELRESPONSE.fields_by_name['sensors'].message_type = _SENSOR
DESCRIPTOR.message_types_by_name['AllSensorsOnVesselRequest'] = _ALLSENSORSONVESSELREQUEST
DESCRIPTOR.message_types_by_name['AllSensorsOnVesselResponse'] = _ALLSENSORSONVESSELRESPONSE
DESCRIPTOR.message_types_by_name['Sensor'] = _SENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AllSensorsOnVesselRequest = _reflection.GeneratedProtocolMessageType('AllSensorsOnVesselRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALLSENSORSONVESSELREQUEST,
  '__module__' : 'sensormanager.sensormanager_pb2'
  # @@protoc_insertion_point(class_scope:sensormanager.AllSensorsOnVesselRequest)
  })
_sym_db.RegisterMessage(AllSensorsOnVesselRequest)

AllSensorsOnVesselResponse = _reflection.GeneratedProtocolMessageType('AllSensorsOnVesselResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALLSENSORSONVESSELRESPONSE,
  '__module__' : 'sensormanager.sensormanager_pb2'
  # @@protoc_insertion_point(class_scope:sensormanager.AllSensorsOnVesselResponse)
  })
_sym_db.RegisterMessage(AllSensorsOnVesselResponse)

Sensor = _reflection.GeneratedProtocolMessageType('Sensor', (_message.Message,), {
  'DESCRIPTOR' : _SENSOR,
  '__module__' : 'sensormanager.sensormanager_pb2'
  # @@protoc_insertion_point(class_scope:sensormanager.Sensor)
  })
_sym_db.RegisterMessage(Sensor)


DESCRIPTOR._options = None

_SENSORMANAGER = _descriptor.ServiceDescriptor(
  name='SensorManager',
  full_name='sensormanager.SensorManager',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=236,
  serialized_end=363,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAllSensorsOnVessel',
    full_name='sensormanager.SensorManager.GetAllSensorsOnVessel',
    index=0,
    containing_service=None,
    input_type=_ALLSENSORSONVESSELREQUEST,
    output_type=_ALLSENSORSONVESSELRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENSORMANAGER)

DESCRIPTOR.services_by_name['SensorManager'] = _SENSORMANAGER

# @@protoc_insertion_point(module_scope)
