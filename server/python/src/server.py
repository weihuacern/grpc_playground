"""The Python implementation of the gRPC server."""

from concurrent import futures

import grpc

import auth_user_pb2 # pylint: disable=import-error
import auth_user_pb2_grpc # pylint: disable=import-error

PORT = 2021

def create_auth_user(request): # pylint: disable=unused-argument
    """
    Input: request, CreateAuthUserRequest
    Output: response, CreateAuthUserReply
    """
    # FIXME, do something # pylint: disable=fixme
    reply = auth_user_pb2.CreateAuthUserReply(
        reply=auth_user_pb2.AuthUserReply(msg="abc"),
    )
    return reply


def read_auth_user(request): # pylint: disable=unused-argument
    """
    Input: request, ReadAuthUserRequest
    Output: response, ReadAuthUserReply
    """
    # FIXME, do something # pylint: disable=fixme
    reply = auth_user_pb2.ReadAuthUserReply(
        reply=auth_user_pb2.AuthUserReply(msg="abc"),
    )
    return reply


def update_auth_user(request): # pylint: disable=unused-argument
    """
    Input: request, UpdateAuthUserRequest
    Output: response, UpdateAuthUserReply
    """
    # FIXME, do something # pylint: disable=fixme
    reply = auth_user_pb2.UpdateAuthUserReply(
        reply=auth_user_pb2.AuthUserReply(msg="abc"),
    )
    return reply


def delete_auth_user(request): # pylint: disable=unused-argument
    """
    Input: request, DeleteAuthUserRequest
    Output: response, DeleteAuthUserReply
    """
    # FIXME, do something # pylint: disable=fixme
    reply = auth_user_pb2.DeleteAuthUserReply(
        reply=auth_user_pb2.AuthUserReply(msg="abc"),
    )
    return reply


class AuthUserServicer(auth_user_pb2_grpc.AuthUserServicer):
    """
    Provides methods that defined in the AuthUser.
    """
    def __init__(self):
        pass

    def CreateAuthUser(self, request, context): # pylint: disable=invalid-name,unused-argument,no-self-use
        """
        Implementation of CreateAuthUser
        """
        response = create_auth_user(request)
        return response

    def ReadAuthUser(self, request, context): # pylint: disable=invalid-name,unused-argument,no-self-use
        """
        Implementation of ReadAuthUser
        """
        response = read_auth_user(request)
        return response

    def UpdateAuthUser(self, request, context): # pylint: disable=invalid-name,unused-argument,no-self-use
        """
        Implementation of UpdateAuthUser
        """
        response = update_auth_user(request)
        return response

    def DeleteAuthUser(self, request, context): # pylint: disable=invalid-name,unused-argument,no-self-use
        """
        Implementation of DeleteAuthUser
        """
        response = delete_auth_user(request)
        return response


def entry():
    """
    server entrypoint
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_user_pb2_grpc.add_AuthUserServicer_to_server(
        AuthUserServicer(), server)
    server.add_insecure_port(f"[::]:{PORT}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    entry()
