# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import carrier_pb2 as carrier__pb2
import empty_pb2 as empty__pb2


class CarrierServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateCarrier = channel.unary_unary(
        '/carrier.CarrierService/CreateCarrier',
        request_serializer=carrier__pb2.CreateCarrierRequest.SerializeToString,
        response_deserializer=carrier__pb2.Carrier.FromString,
        )
    self.GetCarrier = channel.unary_unary(
        '/carrier.CarrierService/GetCarrier',
        request_serializer=carrier__pb2.GetCarrierRequest.SerializeToString,
        response_deserializer=carrier__pb2.Carrier.FromString,
        )
    self.UpdateCarrier = channel.unary_unary(
        '/carrier.CarrierService/UpdateCarrier',
        request_serializer=carrier__pb2.Carrier.SerializeToString,
        response_deserializer=empty__pb2.EmptyResponse.FromString,
        )
    self.DeleteCarrier = channel.unary_unary(
        '/carrier.CarrierService/DeleteCarrier',
        request_serializer=carrier__pb2.DeleteCarrierRequest.SerializeToString,
        response_deserializer=empty__pb2.EmptyResponse.FromString,
        )


class CarrierServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateCarrier(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCarrier(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateCarrier(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteCarrier(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CarrierServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateCarrier': grpc.unary_unary_rpc_method_handler(
          servicer.CreateCarrier,
          request_deserializer=carrier__pb2.CreateCarrierRequest.FromString,
          response_serializer=carrier__pb2.Carrier.SerializeToString,
      ),
      'GetCarrier': grpc.unary_unary_rpc_method_handler(
          servicer.GetCarrier,
          request_deserializer=carrier__pb2.GetCarrierRequest.FromString,
          response_serializer=carrier__pb2.Carrier.SerializeToString,
      ),
      'UpdateCarrier': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateCarrier,
          request_deserializer=carrier__pb2.Carrier.FromString,
          response_serializer=empty__pb2.EmptyResponse.SerializeToString,
      ),
      'DeleteCarrier': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteCarrier,
          request_deserializer=carrier__pb2.DeleteCarrierRequest.FromString,
          response_serializer=empty__pb2.EmptyResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'carrier.CarrierService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
