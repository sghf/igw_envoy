# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/admin/v2alpha/memory.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/admin/v2alpha/memory.proto',
  package='envoy.admin.v2alpha',
  syntax='proto3',
  serialized_pb=_b('\n envoy/admin/v2alpha/memory.proto\x12\x13\x65nvoy.admin.v2alpha\"|\n\x06Memory\x12\x11\n\tallocated\x18\x01 \x01(\x04\x12\x11\n\theap_size\x18\x02 \x01(\x04\x12\x19\n\x11pageheap_unmapped\x18\x03 \x01(\x04\x12\x15\n\rpageheap_free\x18\x04 \x01(\x04\x12\x1a\n\x12total_thread_cache\x18\x05 \x01(\x04\x42\x32\n!io.envoyproxy.envoy.admin.v2alphaB\x0bMemoryProtoP\x01\x62\x06proto3')
)




_MEMORY = _descriptor.Descriptor(
  name='Memory',
  full_name='envoy.admin.v2alpha.Memory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allocated', full_name='envoy.admin.v2alpha.Memory.allocated', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heap_size', full_name='envoy.admin.v2alpha.Memory.heap_size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pageheap_unmapped', full_name='envoy.admin.v2alpha.Memory.pageheap_unmapped', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pageheap_free', full_name='envoy.admin.v2alpha.Memory.pageheap_free', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_thread_cache', full_name='envoy.admin.v2alpha.Memory.total_thread_cache', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=57,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['Memory'] = _MEMORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Memory = _reflection.GeneratedProtocolMessageType('Memory', (_message.Message,), dict(
  DESCRIPTOR = _MEMORY,
  __module__ = 'envoy.admin.v2alpha.memory_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.Memory)
  ))
_sym_db.RegisterMessage(Memory)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!io.envoyproxy.envoy.admin.v2alphaB\013MemoryProtoP\001'))
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