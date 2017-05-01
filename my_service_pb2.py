# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: my_service.proto

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
  name='my_service.proto',
  package='handson',
  syntax='proto3',
  serialized_pb=_b('\n\x10my_service.proto\x12\x07handson\"\'\n\tMyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\"5\n\nMyResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03sex\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\x05\x32{\n\tMyService\x12\x36\n\tMyMethod1\x12\x12.handson.MyRequest\x1a\x13.handson.MyResponse\"\x00\x12\x36\n\tMyMethod2\x12\x12.handson.MyRequest\x1a\x13.handson.MyResponse\"\x00\x42\x32\n\x18\x63om.alexandreesl.handsonB\x0eMyServiceProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MYREQUEST = _descriptor.Descriptor(
  name='MyRequest',
  full_name='handson.MyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='handson.MyRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='handson.MyRequest.code', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=29,
  serialized_end=68,
)


_MYRESPONSE = _descriptor.Descriptor(
  name='MyResponse',
  full_name='handson.MyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='handson.MyResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sex', full_name='handson.MyResponse.sex', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='handson.MyResponse.code', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=70,
  serialized_end=123,
)

DESCRIPTOR.message_types_by_name['MyRequest'] = _MYREQUEST
DESCRIPTOR.message_types_by_name['MyResponse'] = _MYRESPONSE

MyRequest = _reflection.GeneratedProtocolMessageType('MyRequest', (_message.Message,), dict(
  DESCRIPTOR = _MYREQUEST,
  __module__ = 'my_service_pb2'
  # @@protoc_insertion_point(class_scope:handson.MyRequest)
  ))
_sym_db.RegisterMessage(MyRequest)

MyResponse = _reflection.GeneratedProtocolMessageType('MyResponse', (_message.Message,), dict(
  DESCRIPTOR = _MYRESPONSE,
  __module__ = 'my_service_pb2'
  # @@protoc_insertion_point(class_scope:handson.MyResponse)
  ))
_sym_db.RegisterMessage(MyResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030com.alexandreesl.handsonB\016MyServiceProtoP\001\242\002\003HLW'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class MyServiceStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.MyMethod1 = channel.unary_unary(
          '/handson.MyService/MyMethod1',
          request_serializer=MyRequest.SerializeToString,
          response_deserializer=MyResponse.FromString,
          )
      self.MyMethod2 = channel.unary_unary(
          '/handson.MyService/MyMethod2',
          request_serializer=MyRequest.SerializeToString,
          response_deserializer=MyResponse.FromString,
          )


  class MyServiceServicer(object):

    def MyMethod1(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def MyMethod2(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_MyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'MyMethod1': grpc.unary_unary_rpc_method_handler(
            servicer.MyMethod1,
            request_deserializer=MyRequest.FromString,
            response_serializer=MyResponse.SerializeToString,
        ),
        'MyMethod2': grpc.unary_unary_rpc_method_handler(
            servicer.MyMethod2,
            request_deserializer=MyRequest.FromString,
            response_serializer=MyResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'handson.MyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaMyServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def MyMethod1(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def MyMethod2(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaMyServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def MyMethod1(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    MyMethod1.future = None
    def MyMethod2(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    MyMethod2.future = None


  def beta_create_MyService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('handson.MyService', 'MyMethod1'): MyRequest.FromString,
      ('handson.MyService', 'MyMethod2'): MyRequest.FromString,
    }
    response_serializers = {
      ('handson.MyService', 'MyMethod1'): MyResponse.SerializeToString,
      ('handson.MyService', 'MyMethod2'): MyResponse.SerializeToString,
    }
    method_implementations = {
      ('handson.MyService', 'MyMethod1'): face_utilities.unary_unary_inline(servicer.MyMethod1),
      ('handson.MyService', 'MyMethod2'): face_utilities.unary_unary_inline(servicer.MyMethod2),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_MyService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('handson.MyService', 'MyMethod1'): MyRequest.SerializeToString,
      ('handson.MyService', 'MyMethod2'): MyRequest.SerializeToString,
    }
    response_deserializers = {
      ('handson.MyService', 'MyMethod1'): MyResponse.FromString,
      ('handson.MyService', 'MyMethod2'): MyResponse.FromString,
    }
    cardinalities = {
      'MyMethod1': cardinality.Cardinality.UNARY_UNARY,
      'MyMethod2': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'handson.MyService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
