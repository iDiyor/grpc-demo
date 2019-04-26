# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: carrier.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='carrier.proto',
  package='carrier',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rcarrier.proto\x12\x07\x63\x61rrier\"L\n\x07\x43\x61rrier\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cphone_number\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\t\":\n\x14\x43reateCarrierRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cphone_number\x18\x02 \x01(\tb\x06proto3')
)




_CARRIER = _descriptor.Descriptor(
  name='Carrier',
  full_name='carrier.Carrier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='carrier.Carrier.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='carrier.Carrier.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='carrier.Carrier.phone_number', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='carrier.Carrier.timestamp', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=26,
  serialized_end=102,
)


_CREATECARRIERREQUEST = _descriptor.Descriptor(
  name='CreateCarrierRequest',
  full_name='carrier.CreateCarrierRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='carrier.CreateCarrierRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='carrier.CreateCarrierRequest.phone_number', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=104,
  serialized_end=162,
)

DESCRIPTOR.message_types_by_name['Carrier'] = _CARRIER
DESCRIPTOR.message_types_by_name['CreateCarrierRequest'] = _CREATECARRIERREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Carrier = _reflection.GeneratedProtocolMessageType('Carrier', (_message.Message,), dict(
  DESCRIPTOR = _CARRIER,
  __module__ = 'carrier_pb2'
  # @@protoc_insertion_point(class_scope:carrier.Carrier)
  ))
_sym_db.RegisterMessage(Carrier)

CreateCarrierRequest = _reflection.GeneratedProtocolMessageType('CreateCarrierRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATECARRIERREQUEST,
  __module__ = 'carrier_pb2'
  # @@protoc_insertion_point(class_scope:carrier.CreateCarrierRequest)
  ))
_sym_db.RegisterMessage(CreateCarrierRequest)


# @@protoc_insertion_point(module_scope)
