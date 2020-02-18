"""The Python implementation of the gRPC client."""

from __future__ import print_function

import grpc

import auth_user_pb2 # pylint: disable=import-error
import auth_user_pb2_grpc # pylint: disable=import-error

PORT = 2021

def auth_user_create_auth_user(stub):
    """
    Test client function for CreateAuthUser
    """
    # FIXME, do something # pylint: disable=fixme
    request = auth_user_pb2.CreateAuthUserRequest()
    reply = stub.CreateAuthUser(request)
    print(reply.reply.msg)


def auth_user_read_auth_user(stub):
    """
    Test client function for ReadAuthUser
    """
    # FIXME, do something # pylint: disable=fixme
    request = auth_user_pb2.ReadAuthUserRequest()
    reply = stub.ReadAuthUser(request)
    print(reply.reply.msg)


def auth_user_update_auth_user(stub):
    """
    Test client function for UpdateAuthUser
    """
    # FIXME, do something # pylint: disable=fixme
    request = auth_user_pb2.UpdateAuthUserRequest()
    reply = stub.UpdateAuthUser(request)
    print(reply.reply.msg)


def auth_user_delete_auth_user(stub):
    """
    Test client function for DeleteAuthUser
    """
    # FIXME, do something # pylint: disable=fixme
    request = auth_user_pb2.DeleteAuthUserRequest()
    reply = stub.DeleteAuthUser(request)
    print(reply.reply.msg)


def entry():
    """
    Client entrypoint
    """
    with grpc.insecure_channel(f"localhost:{PORT}") as channel:
        stub = auth_user_pb2_grpc.AuthUserStub(channel)
        print("-------------- CreateAuthUser --------------")
        auth_user_create_auth_user(stub)
        print("-------------- ReadAuthUser --------------")
        auth_user_read_auth_user(stub)
        print("-------------- UpdateAuthUser --------------")
        auth_user_update_auth_user(stub)
        print("-------------- DeleteAuthUser --------------")
        auth_user_delete_auth_user(stub)


if __name__ == '__main__':
    entry()
