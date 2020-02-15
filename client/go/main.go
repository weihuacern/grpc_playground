package main

import (
	"context"
	"fmt"
	"os"
	"strconv"
	"time"

	"google.golang.org/grpc"

	pb "message"
)

const (
	port = 2021
)

// RequestType : the type of request
type RequestType int

const (
	// CreateAuthUser : create an user
	CreateAuthUser RequestType = iota
	// ReadAuthUser : get an array of users
	ReadAuthUser
	// UpdateAuthUser : update an user
	UpdateAuthUser
	// DeleteAuthUser : delete an user
	DeleteAuthUser
)

func main() {
	// gRPC connection
	conn, err := grpc.Dial(fmt.Sprintf("localhost:%d", port), grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		fmt.Printf("Error when connect: %s\n", err.Error())
	}
	defer conn.Close()

	// gRPC client
	client := pb.NewAuthUserClient(conn)

	// context
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	// Input parameter
	var reqType RequestType
	if len(os.Args) > 1 {
		if num, err := strconv.Atoi(os.Args[1]); err == nil {
			reqType = RequestType(num)
		} else {
			fmt.Printf("Invaid input parameters: %s; Error: %s\n", os.Args[1], err.Error())
			return
		}
	} else {
		fmt.Printf("Invaid input parameters error: %s\n", err.Error())
		return
	}

	switch reqType {
	case CreateAuthUser:
		r, err := client.CreateAuthUser(ctx, &pb.CreateAuthUserRequest{})
		if err != nil {
			fmt.Printf("Error: %s\n", err.Error())
		}
		fmt.Printf("Response: %v\n", r)
	case ReadAuthUser:
		r, err := client.ReadAuthUser(ctx, &pb.ReadAuthUserRequest{})
		if err != nil {
			fmt.Printf("Error: %s\n", err.Error())
		}
		fmt.Printf("Response: %v\n", r)
	case UpdateAuthUser:
		r, err := client.UpdateAuthUser(ctx, &pb.UpdateAuthUserRequest{})
		if err != nil {
			fmt.Printf("Error: %s\n", err.Error())
		}
		fmt.Printf("Response: %v\n", r)
	case DeleteAuthUser:
		r, err := client.DeleteAuthUser(ctx, &pb.DeleteAuthUserRequest{})
		if err != nil {
			fmt.Printf("Error: %s\n", err.Error())
		}
		fmt.Printf("Response: %v\n", r)
	}
}
