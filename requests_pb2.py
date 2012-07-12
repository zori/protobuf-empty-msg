# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2



_REQUEST = descriptor.Descriptor(
  name='Request',
  full_name='req.Request',
  filename='requests.proto',
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_TAGGINGREQUEST = descriptor.Descriptor(
  name='TaggingRequest',
  full_name='req.TaggingRequest',
  filename='requests.proto',
  containing_type=None,
  fields=[
  ],
  extensions=[
    descriptor.FieldDescriptor(
      name='tagging', full_name='req.TaggingRequest.tagging', index=0,
      number=1, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_NUMBEREDREQUEST = descriptor.Descriptor(
  name='NumberedRequest',
  full_name='req.NumberedRequest',
  filename='requests.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='number', full_name='req.NumberedRequest.number', index=0,
      number=1, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    descriptor.FieldDescriptor(
      name='numbered', full_name='req.NumberedRequest.numbered', index=0,
      number=2, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)



class Request(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUEST

class TaggingRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAGGINGREQUEST

class NumberedRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NUMBEREDREQUEST

_TAGGINGREQUEST.extensions_by_name['tagging'].message_type = _TAGGINGREQUEST
Request.RegisterExtension(_TAGGINGREQUEST.extensions_by_name['tagging'])
_NUMBEREDREQUEST.extensions_by_name['numbered'].message_type = _NUMBEREDREQUEST
Request.RegisterExtension(_NUMBEREDREQUEST.extensions_by_name['numbered'])