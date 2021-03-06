# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/overload/v2alpha/overload.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/overload/v2alpha/overload.proto',
  package='envoy.config.overload.v2alpha',
  syntax='proto3',
  serialized_pb=_b('\n,envoy/config/overload/v2alpha/overload.proto\x12\x1d\x65nvoy.config.overload.v2alpha\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x17validate/validate.proto\"\x96\x01\n\x0fResourceMonitor\x12\x17\n\x04name\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12-\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructB\x02\x18\x01H\x00\x12,\n\x0ctyped_config\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\r\n\x0b\x63onfig_type\"<\n\x10ThresholdTrigger\x12(\n\x05value\x18\x01 \x01(\x01\x42\x19\xba\xe9\xc0\x03\x14\x12\x12\x19\x00\x00\x00\x00\x00\x00\xf0?)\x00\x00\x00\x00\x00\x00\x00\x00\"\x80\x01\n\x07Trigger\x12\x17\n\x04name\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12\x44\n\tthreshold\x18\x02 \x01(\x0b\x32/.envoy.config.overload.v2alpha.ThresholdTriggerH\x00\x42\x16\n\rtrigger_oneof\x12\x05\xb8\xe9\xc0\x03\x01\"o\n\x0eOverloadAction\x12\x17\n\x04name\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12\x44\n\x08triggers\x18\x02 \x03(\x0b\x32&.envoy.config.overload.v2alpha.TriggerB\n\xba\xe9\xc0\x03\x05\x92\x01\x02\x08\x01\"\xdd\x01\n\x0fOverloadManager\x12\x33\n\x10refresh_interval\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12U\n\x11resource_monitors\x18\x02 \x03(\x0b\x32..envoy.config.overload.v2alpha.ResourceMonitorB\n\xba\xe9\xc0\x03\x05\x92\x01\x02\x08\x01\x12>\n\x07\x61\x63tions\x18\x03 \x03(\x0b\x32-.envoy.config.overload.v2alpha.OverloadActionBG\n+io.envoyproxy.envoy.config.overload.v2alphaB\rOverloadProtoP\x01Z\x07v2alphab\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_RESOURCEMONITOR = _descriptor.Descriptor(
  name='ResourceMonitor',
  full_name='envoy.config.overload.v2alpha.ResourceMonitor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='envoy.config.overload.v2alpha.ResourceMonitor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='config', full_name='envoy.config.overload.v2alpha.ResourceMonitor.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='typed_config', full_name='envoy.config.overload.v2alpha.ResourceMonitor.typed_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='config_type', full_name='envoy.config.overload.v2alpha.ResourceMonitor.config_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=194,
  serialized_end=344,
)


_THRESHOLDTRIGGER = _descriptor.Descriptor(
  name='ThresholdTrigger',
  full_name='envoy.config.overload.v2alpha.ThresholdTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='envoy.config.overload.v2alpha.ThresholdTrigger.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\024\022\022\031\000\000\000\000\000\000\360?)\000\000\000\000\000\000\000\000'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=406,
)


_TRIGGER = _descriptor.Descriptor(
  name='Trigger',
  full_name='envoy.config.overload.v2alpha.Trigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='envoy.config.overload.v2alpha.Trigger.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='envoy.config.overload.v2alpha.Trigger.threshold', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='trigger_oneof', full_name='envoy.config.overload.v2alpha.Trigger.trigger_oneof',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=409,
  serialized_end=537,
)


_OVERLOADACTION = _descriptor.Descriptor(
  name='OverloadAction',
  full_name='envoy.config.overload.v2alpha.OverloadAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='envoy.config.overload.v2alpha.OverloadAction.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='triggers', full_name='envoy.config.overload.v2alpha.OverloadAction.triggers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=539,
  serialized_end=650,
)


_OVERLOADMANAGER = _descriptor.Descriptor(
  name='OverloadManager',
  full_name='envoy.config.overload.v2alpha.OverloadManager',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='refresh_interval', full_name='envoy.config.overload.v2alpha.OverloadManager.refresh_interval', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource_monitors', full_name='envoy.config.overload.v2alpha.OverloadManager.resource_monitors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='actions', full_name='envoy.config.overload.v2alpha.OverloadManager.actions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=653,
  serialized_end=874,
)

_RESOURCEMONITOR.fields_by_name['config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_RESOURCEMONITOR.fields_by_name['typed_config'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_RESOURCEMONITOR.oneofs_by_name['config_type'].fields.append(
  _RESOURCEMONITOR.fields_by_name['config'])
_RESOURCEMONITOR.fields_by_name['config'].containing_oneof = _RESOURCEMONITOR.oneofs_by_name['config_type']
_RESOURCEMONITOR.oneofs_by_name['config_type'].fields.append(
  _RESOURCEMONITOR.fields_by_name['typed_config'])
_RESOURCEMONITOR.fields_by_name['typed_config'].containing_oneof = _RESOURCEMONITOR.oneofs_by_name['config_type']
_TRIGGER.fields_by_name['threshold'].message_type = _THRESHOLDTRIGGER
_TRIGGER.oneofs_by_name['trigger_oneof'].fields.append(
  _TRIGGER.fields_by_name['threshold'])
_TRIGGER.fields_by_name['threshold'].containing_oneof = _TRIGGER.oneofs_by_name['trigger_oneof']
_OVERLOADACTION.fields_by_name['triggers'].message_type = _TRIGGER
_OVERLOADMANAGER.fields_by_name['refresh_interval'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_OVERLOADMANAGER.fields_by_name['resource_monitors'].message_type = _RESOURCEMONITOR
_OVERLOADMANAGER.fields_by_name['actions'].message_type = _OVERLOADACTION
DESCRIPTOR.message_types_by_name['ResourceMonitor'] = _RESOURCEMONITOR
DESCRIPTOR.message_types_by_name['ThresholdTrigger'] = _THRESHOLDTRIGGER
DESCRIPTOR.message_types_by_name['Trigger'] = _TRIGGER
DESCRIPTOR.message_types_by_name['OverloadAction'] = _OVERLOADACTION
DESCRIPTOR.message_types_by_name['OverloadManager'] = _OVERLOADMANAGER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourceMonitor = _reflection.GeneratedProtocolMessageType('ResourceMonitor', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCEMONITOR,
  __module__ = 'envoy.config.overload.v2alpha.overload_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.overload.v2alpha.ResourceMonitor)
  ))
_sym_db.RegisterMessage(ResourceMonitor)

ThresholdTrigger = _reflection.GeneratedProtocolMessageType('ThresholdTrigger', (_message.Message,), dict(
  DESCRIPTOR = _THRESHOLDTRIGGER,
  __module__ = 'envoy.config.overload.v2alpha.overload_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.overload.v2alpha.ThresholdTrigger)
  ))
_sym_db.RegisterMessage(ThresholdTrigger)

Trigger = _reflection.GeneratedProtocolMessageType('Trigger', (_message.Message,), dict(
  DESCRIPTOR = _TRIGGER,
  __module__ = 'envoy.config.overload.v2alpha.overload_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.overload.v2alpha.Trigger)
  ))
_sym_db.RegisterMessage(Trigger)

OverloadAction = _reflection.GeneratedProtocolMessageType('OverloadAction', (_message.Message,), dict(
  DESCRIPTOR = _OVERLOADACTION,
  __module__ = 'envoy.config.overload.v2alpha.overload_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.overload.v2alpha.OverloadAction)
  ))
_sym_db.RegisterMessage(OverloadAction)

OverloadManager = _reflection.GeneratedProtocolMessageType('OverloadManager', (_message.Message,), dict(
  DESCRIPTOR = _OVERLOADMANAGER,
  __module__ = 'envoy.config.overload.v2alpha.overload_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.overload.v2alpha.OverloadManager)
  ))
_sym_db.RegisterMessage(OverloadManager)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n+io.envoyproxy.envoy.config.overload.v2alphaB\rOverloadProtoP\001Z\007v2alpha'))
_RESOURCEMONITOR.fields_by_name['name'].has_options = True
_RESOURCEMONITOR.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_RESOURCEMONITOR.fields_by_name['config'].has_options = True
_RESOURCEMONITOR.fields_by_name['config']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_THRESHOLDTRIGGER.fields_by_name['value'].has_options = True
_THRESHOLDTRIGGER.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\024\022\022\031\000\000\000\000\000\000\360?)\000\000\000\000\000\000\000\000'))
_TRIGGER.oneofs_by_name['trigger_oneof'].has_options = True
_TRIGGER.oneofs_by_name['trigger_oneof']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_TRIGGER.fields_by_name['name'].has_options = True
_TRIGGER.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_OVERLOADACTION.fields_by_name['name'].has_options = True
_OVERLOADACTION.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_OVERLOADACTION.fields_by_name['triggers'].has_options = True
_OVERLOADACTION.fields_by_name['triggers']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))
_OVERLOADMANAGER.fields_by_name['resource_monitors'].has_options = True
_OVERLOADMANAGER.fields_by_name['resource_monitors']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
