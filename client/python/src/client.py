from __future__ import print_function

import random

import grpc

import auth_user_pb2 # pylint: disable=import-error
import auth_user_pb2_grpc # pylint: disable=import-error

PORT = 2021

def auth_user_CreateAuthUser(stub):
    """
    Test client function for CreateAuthUser
    """
    # TODO, do something
    request = auth_user_pb2.CreateAuthUserRequest()
    reply = stub.CreateAuthUser(request)
    print(reply.reply.msg)


def auth_user_ReadAuthUser(stub):
    """
    Test client function for ReadAuthUser
    """
    # TODO, do something
    request = auth_user_pb2.ReadAuthUserRequest()
    reply = stub.ReadAuthUser(request)
    print(reply.reply.msg)


def auth_user_UpdateAuthUser(stub):
    """
    Test client function for UpdateAuthUser
    """
    # TODO, do something
    request = auth_user_pb2.UpdateAuthUserRequest()
    reply = stub.UpdateAuthUser(request)
    print(reply.reply.msg)


def auth_user_DeleteAuthUser(stub):
    """
    Test client function for DeleteAuthUser
    """
    # TODO, do something
    request = auth_user_pb2.DeleteAuthUserRequest()
    reply = stub.DeleteAuthUser(request)
    print(reply.reply.msg)


def entry():
    with grpc.insecure_channel(f"localhost:{PORT}") as channel:
        stub = auth_user_pb2_grpc.AuthUserStub(channel)
        print("-------------- CreateAuthUser --------------")
        auth_user_CreateAuthUser(stub)
        print("-------------- ReadAuthUser --------------")
        auth_user_ReadAuthUser(stub)
        print("-------------- UpdateAuthUser --------------")
        auth_user_UpdateAuthUser(stub)
        print("-------------- DeleteAuthUser --------------")
        auth_user_DeleteAuthUser(stub)


if __name__ == '__main__':
    entry()