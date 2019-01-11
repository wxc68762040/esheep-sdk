# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import api_pb2 as api__pb2


class EsheepAgentStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.createRoom = channel.unary_unary(
        '/org.seekloud.esheepapi.pb.EsheepAgent/createRoom',
        request_serializer=api__pb2.CreateRoomReq.SerializeToString,
        response_deserializer=api__pb2.CreateRoomRsp.FromString,
        )
    self.joinRoom = channel.unary_unary(
        '/org.seekloud.esheepapi.pb.EsheepAgent/joinRoom',
        request_serializer=api__pb2.JoinRoomReq.SerializeToString,
        response_deserializer=api__pb2.SimpleRsp.FromString,
        )
    self.leaveRoom = channel.unary_unary(
        '/org.seekloud.esheepapi.pb.EsheepAgent/leaveRoom',
        request_serializer=api__pb2.Credit.SerializeToString,
        response_deserializer=api__pb2.SimpleRsp.FromString,
        )
    self.actionSpace = channel.unary_unary(
        '/org.seekloud.esheepapi.pb.EsheepAgent/actionSpace',
        request_serializer=api__pb2.Credit.SerializeToString,
        response_deserializer=api__pb2.ActionSpaceRsp.FromString,
        )
    self.systemInfo = channel.unary_unary(
        '/org.seekloud.esheepapi.pb.EsheepAgent/systemInfo',
        request_serializer=api__pb2.Credit.SerializeToString,
        response_deserializer=api__pb2.SystemInfoRsp.FromString,
        )
    self.action = channel.unary_unary(
        '/org.seekloud.esheepapi.pb.EsheepAgent/action',
        request_serializer=api__pb2.ActionReq.SerializeToString,
        response_deserializer=api__pb2.ActionRsp.FromString,
        )
    self.observation = channel.unary_unary(
        '/org.seekloud.esheepapi.pb.EsheepAgent/observation',
        request_serializer=api__pb2.Credit.SerializeToString,
        response_deserializer=api__pb2.ObservationRsp.FromString,
        )
    self.inform = channel.unary_unary(
        '/org.seekloud.esheepapi.pb.EsheepAgent/inform',
        request_serializer=api__pb2.Credit.SerializeToString,
        response_deserializer=api__pb2.InformRsp.FromString,
        )
    self.reincarnation = channel.unary_unary(
        '/org.seekloud.esheepapi.pb.EsheepAgent/reincarnation',
        request_serializer=api__pb2.Credit.SerializeToString,
        response_deserializer=api__pb2.SimpleRsp.FromString,
        )
    self.currentFrame = channel.unary_unary(
        '/org.seekloud.esheepapi.pb.EsheepAgent/currentFrame',
        request_serializer=api__pb2.Credit.SerializeToString,
        response_deserializer=api__pb2.CurrentFrameRsp.FromString,
        )


class EsheepAgentServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def createRoom(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def joinRoom(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def leaveRoom(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def actionSpace(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def systemInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def action(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def observation(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def inform(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def reincarnation(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def currentFrame(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EsheepAgentServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'createRoom': grpc.unary_unary_rpc_method_handler(
          servicer.createRoom,
          request_deserializer=api__pb2.CreateRoomReq.FromString,
          response_serializer=api__pb2.CreateRoomRsp.SerializeToString,
      ),
      'joinRoom': grpc.unary_unary_rpc_method_handler(
          servicer.joinRoom,
          request_deserializer=api__pb2.JoinRoomReq.FromString,
          response_serializer=api__pb2.SimpleRsp.SerializeToString,
      ),
      'leaveRoom': grpc.unary_unary_rpc_method_handler(
          servicer.leaveRoom,
          request_deserializer=api__pb2.Credit.FromString,
          response_serializer=api__pb2.SimpleRsp.SerializeToString,
      ),
      'actionSpace': grpc.unary_unary_rpc_method_handler(
          servicer.actionSpace,
          request_deserializer=api__pb2.Credit.FromString,
          response_serializer=api__pb2.ActionSpaceRsp.SerializeToString,
      ),
      'systemInfo': grpc.unary_unary_rpc_method_handler(
          servicer.systemInfo,
          request_deserializer=api__pb2.Credit.FromString,
          response_serializer=api__pb2.SystemInfoRsp.SerializeToString,
      ),
      'action': grpc.unary_unary_rpc_method_handler(
          servicer.action,
          request_deserializer=api__pb2.ActionReq.FromString,
          response_serializer=api__pb2.ActionRsp.SerializeToString,
      ),
      'observation': grpc.unary_unary_rpc_method_handler(
          servicer.observation,
          request_deserializer=api__pb2.Credit.FromString,
          response_serializer=api__pb2.ObservationRsp.SerializeToString,
      ),
      'inform': grpc.unary_unary_rpc_method_handler(
          servicer.inform,
          request_deserializer=api__pb2.Credit.FromString,
          response_serializer=api__pb2.InformRsp.SerializeToString,
      ),
      'reincarnation': grpc.unary_unary_rpc_method_handler(
          servicer.reincarnation,
          request_deserializer=api__pb2.Credit.FromString,
          response_serializer=api__pb2.SimpleRsp.SerializeToString,
      ),
      'currentFrame': grpc.unary_unary_rpc_method_handler(
          servicer.currentFrame,
          request_deserializer=api__pb2.Credit.FromString,
          response_serializer=api__pb2.CurrentFrameRsp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'org.seekloud.esheepapi.pb.EsheepAgent', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
