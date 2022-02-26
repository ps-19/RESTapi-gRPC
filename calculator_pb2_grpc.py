# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calculator_pb2 as calculator__pb2


class YourServiceStub(object):
    """service Calculator{
    rpc Sum(Number) returns (Number) {}
    }

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Sum = channel.unary_unary(
                '/YourService/Sum',
                request_serializer=calculator__pb2.Number.SerializeToString,
                response_deserializer=calculator__pb2.Number.FromString,
                )


class YourServiceServicer(object):
    """service Calculator{
    rpc Sum(Number) returns (Number) {}
    }

    """

    def Sum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_YourServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Sum': grpc.unary_unary_rpc_method_handler(
                    servicer.Sum,
                    request_deserializer=calculator__pb2.Number.FromString,
                    response_serializer=calculator__pb2.Number.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'YourService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class YourService(object):
    """service Calculator{
    rpc Sum(Number) returns (Number) {}
    }

    """

    @staticmethod
    def Sum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YourService/Sum',
            calculator__pb2.Number.SerializeToString,
            calculator__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
