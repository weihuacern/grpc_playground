package com.example.grpc;

import io.grpc.Channel;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;
import java.util.concurrent.TimeUnit;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * A simple client.
 */
public class AuthUserClient {
    private static final Logger logger = Logger.getLogger(AuthUserClient.class.getName());
    
    private final AuthUserGrpc.AuthUserBlockingStub blockingStub;
    
    public AuthUserClient(Channel channel) {
        blockingStub = AuthUserGrpc.newBlockingStub(channel);
    }
    
    enum RequestType 
    { 
        CreateAuthUser, ReadAuthUser, UpdateAuthUser, DeleteAuthUser; 
    } 

    public void call(RequestType reqType) {
        switch(reqType) {
            case CreateAuthUser: {
                CreateAuthUserRequest request = CreateAuthUserRequest.newBuilder().build();
                CreateAuthUserReply response;
                try {
                    response = blockingStub.createAuthUser(request);
                } catch (StatusRuntimeException e) {
                    logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
                    return;
                }
                logger.info("CreateAuthUser: " + response.getReply().getMsg());
                return;
            }
            case ReadAuthUser: {
                ReadAuthUserRequest request = ReadAuthUserRequest.newBuilder().build();
                ReadAuthUserReply response;
                try {
                    response = blockingStub.readAuthUser(request);
                } catch (StatusRuntimeException e) {
                    logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
                    return;
                }
                logger.info("ReadAuthUser: " + response.getReply().getMsg());
                return;
            }
            case UpdateAuthUser: {
                UpdateAuthUserRequest request = UpdateAuthUserRequest.newBuilder().build();
                UpdateAuthUserReply response;
                try {
                    response = blockingStub.updateAuthUser(request);
                } catch (StatusRuntimeException e) {
                    logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
                    return;
                }
                logger.info("UpdateAuthUser: " + response.getReply().getMsg());
                return;
            }
            default: {
                DeleteAuthUserRequest request = DeleteAuthUserRequest.newBuilder().build();
                DeleteAuthUserReply response;
                try {
                    response = blockingStub.deleteAuthUser(request);
                } catch (StatusRuntimeException e) {
                    logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
                    return;
                }
                logger.info("DeleteAuthUser: " + response.getReply().getMsg());
                return;
            }
        }
    }

    /**
     * AuthUserClient.
     */
    public static void main(String[] args) throws Exception {
        String reqType = "1";
        int port = 2021;
        String target = "localhost:2021";
        // Allow passing in the user and target strings as command line arguments
        if (args.length > 0) {
            if ("--help".equals(args[0])) {
                System.err.println("Usage: [RequestType]");
                System.err.println("");
                System.err.println("  RequestType: The type of gRPC request that client will query; Default is: " + reqType);
                System.exit(1);
            }
            reqType = args[0];
        }

        // Create a communication channel to the server, known as a Channel. Channels are thread-safe
        // and reusable. It is common to create channels at the beginning of your application and reuse
        // them until the application shuts down.
        ManagedChannel channel = ManagedChannelBuilder.forTarget(String.format("localhost:%d", port)).usePlaintext().build();
        try {
            AuthUserClient client = new AuthUserClient(channel);
            RequestType reqTypeEnum = RequestType.values()[Integer.parseInt(reqType)];
            client.call(reqTypeEnum);
        } finally {
            channel.shutdownNow().awaitTermination(5, TimeUnit.SECONDS);
        }
    }
}