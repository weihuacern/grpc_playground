package server

import (
	"context"
	"fmt"
	"net"

	"google.golang.org/grpc"

	pb "message"
)

const (
	port = 2021
)

type gRPCMethod struct {
	pb.UnimplementedAuthUserServer
}

// CreateAuthUser : RPC method to create user
func (as *gRPCMethod) CreateAuthUser(ctx context.Context, in *pb.CreateAuthUserRequest) (*pb.CreateAuthUserReply, error) {
	// TODO, do someting
	return &pb.CreateAuthUserReply{Reply: &pb.AuthUserReply{Msg: "abc"}}, nil
}

// ReadAuthUser : RPC method to read user
func (as *gRPCMethod) ReadAuthUser(ctx context.Context, in *pb.ReadAuthUserRequest) (*pb.ReadAuthUserReply, error) {
	// TODO, do someting
	return &pb.ReadAuthUserReply{Reply: &pb.AuthUserReply{Msg: "abc"}}, nil
}

// UpdateAuthUser : RPC method to update user
func (as *gRPCMethod) UpdateAuthUser(ctx context.Context, in *pb.UpdateAuthUserRequest) (*pb.UpdateAuthUserReply, error) {
	// TODO, do someting
	return &pb.UpdateAuthUserReply{Reply: &pb.AuthUserReply{Msg: "abc"}}, nil
}

// DeleteAuthUser : RPC method to delete user
func (as *gRPCMethod) DeleteAuthUser(ctx context.Context, in *pb.DeleteAuthUserRequest) (*pb.DeleteAuthUserReply, error) {
	// TODO, do someting
	return &pb.DeleteAuthUserReply{Reply: &pb.AuthUserReply{Msg: "abc"}}, nil
}

// AuthServer : gRPC server for authentication and authorization
type AuthServer struct {
	server *grpc.Server
	method *gRPCMethod
}

// Init : Initialize gRPC server
func (as *AuthServer) Init() {
	as.server = grpc.NewServer()
	as.method = &gRPCMethod{}
	pb.RegisterAuthUserServer(as.server, as.method)
}

// Work : Run gRPC server
func (as *AuthServer) Work() {
	var listen net.Listener
	var err error
	if listen, err = net.Listen("tcp", fmt.Sprintf(":%d", port)); err != nil {
		fmt.Printf("Failed to listen: %s\n", err.Error())
		return
	}

	if err = as.server.Serve(listen); err != nil {
		fmt.Printf("Failed to serve: %s\n", err.Error())
	} else {
		fmt.Printf("Server started at Port[%d]\n", port)
	}

}

// NewAuthServer : Entrypoint to create new gRPC service
func NewAuthServer() (*AuthServer, error) {
	var as AuthServer
	return &as, nil
}
