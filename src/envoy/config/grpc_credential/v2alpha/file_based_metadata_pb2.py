# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/grpc_credential/v2alpha/file_based_metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.api.v2.core import base_pb2 as envoy_dot_api_dot_v2_dot_core_dot_base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/grpc_credential/v2alpha/file_based_metadata.proto',
  package='envoy.config.grpc_credential.v2alpha',
  syntax='proto3',
  serialized_pb=_b('\n>envoy/config/grpc_credential/v2alpha/file_based_metadata.proto\x12$envoy.config.grpc_credential.v2alpha\x1a\x1c\x65nvoy/api/v2/core/base.proto\"x\n\x17\x46ileBasedMetadataConfig\x12\x32\n\x0bsecret_data\x18\x01 \x01(\x0b\x32\x1d.envoy.api.v2.core.DataSource\x12\x12\n\nheader_key\x18\x02 \x01(\t\x12\x15\n\rheader_prefix\x18\x03 \x01(\tBW\n2io.envoyproxy.envoy.config.grpc_credential.v2alphaB\x16\x46ileBasedMetadataProtoP\x01Z\x07v2alphab\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_core_dot_base__pb2.DESCRIPTOR,])




_FILEBASEDMETADATACONFIG = _descriptor.Descriptor(
  name='FileBasedMetadataConfig',
  full_name='envoy.config.grpc_credential.v2alpha.FileBasedMetadataConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret_data', full_name='envoy.config.grpc_credential.v2alpha.FileBasedMetadataConfig.secret_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header_key', full_name='envoy.config.grpc_credential.v2alpha.FileBasedMetadataConfig.header_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header_prefix', full_name='envoy.config.grpc_credential.v2alpha.FileBasedMetadataConfig.header_prefix', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=134,
  serialized_end=254,
)

_FILEBASEDMETADATACONFIG.fields_by_name['secret_data'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._DATASOURCE
DESCRIPTOR.message_types_by_name['FileBasedMetadataConfig'] = _FILEBASEDMETADATACONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileBasedMetadataConfig = _reflection.GeneratedProtocolMessageType('FileBasedMetadataConfig', (_message.Message,), dict(
  DESCRIPTOR = _FILEBASEDMETADATACONFIG,
  __module__ = 'envoy.config.grpc_credential.v2alpha.file_based_metadata_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.grpc_credential.v2alpha.FileBasedMetadataConfig)
  ))
_sym_db.RegisterMessage(FileBasedMetadataConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n2io.envoyproxy.envoy.config.grpc_credential.v2alphaB\026FileBasedMetadataProtoP\001Z\007v2alpha'))
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
