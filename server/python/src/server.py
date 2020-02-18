from concurrent import futures
import math
import time

import grpc

import auth_user_pb2 # pylint: disable=import-error
import auth_user_pb2_grpc # pylint: disable=import-error

PORT = 2021

def create_auth_user(request):
    """
    Input: request, CreateAuthUserRequest
    Output: response, CreateAuthUserReply
    """
    # TODO, do something
    reply = auth_user_pb2.CreateAuthUserReply(
        reply=auth_user_pb2.AuthUserReply(msg="abc"),
    )
    return reply


def read_auth_user(request):
    """
    Input: request, ReadAuthUserRequest
    Output: response, ReadAuthUserReply
    """
    # TODO, do something
    reply = auth_user_pb2.ReadAuthUserReply(
        reply=auth_user_pb2.AuthUserReply(msg="abc"),
    )
    return reply


def update_auth_user(request):
    """
    Input: request, UpdateAuthUserRequest
    Output: response, UpdateAuthUserReply
    """
    # TODO, do something
    reply = auth_user_pb2.UpdateAuthUserReply(
        reply=auth_user_pb2.AuthUserReply(msg="abc"),
    )
    return reply


def delete_auth_user(request):
    """
    Input: request, DeleteAuthUserRequest
    Output: response, DeleteAuthUserReply
    """
    # TODO, do something
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

    def CreateAuthUser(self, request, context):
        response = create_auth_user(request)
        return response

    def ReadAuthUser(self, request, context):
        response = read_auth_user(request)
        return response

    def UpdateAuthUser(self, request, context):
        response = update_auth_user(request)
        return response

    def DeleteAuthUser(self, request, context):
        response = delete_auth_user(request)
        return response


def entry():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_user_pb2_grpc.add_AuthUserServicer_to_server(
        AuthUserServicer(), server)
    server.add_insecure_port(f"[::]:{PORT}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    entry()