package com.example.grpc;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import java.io.IOException;
import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;

/**
 * Server that manages startup/shutdown of a AuthUser server.
 */
public class AuthUserServer {
    private static final Logger logger = Logger.getLogger(AuthUserServer.class.getName());
    
    private Server server;
    
    private void start() throws IOException {
        /* The port on which the server should run */
        int port = 2021;
        server = ServerBuilder.forPort(port)
        .addService(new AuthUserImpl())
        .build()
        .start();
        
        logger.info("Server started, listening on " + port);
        
        Runtime.getRuntime().addShutdownHook(new Thread() {
            @Override
            public void run() {
                // Use stderr here since the logger may have been reset by its JVM shutdown hook.
                System.err.println("*** shutting down gRPC server since JVM is shutting down");
                try {
                    AuthUserServer.this.stop();
                } catch (InterruptedException e) {
                    e.printStackTrace(System.err);
                }
                System.err.println("*** server shut down");
            }
        });
    }
    
    private void stop() throws InterruptedException {
        if (server != null) {
            server.shutdown().awaitTermination(30, TimeUnit.SECONDS);
        }
    }
    
    /**
     * Await termination on the main thread since the grpc library uses daemon threads.
     */
    private void blockUntilShutdown() throws InterruptedException {
        if (server != null) {
            server.awaitTermination();
        }
    }

    /**
     * Main launches the server from the command line.
     */
    public static void main(String[] args) throws IOException, InterruptedException {
        final AuthUserServer server = new AuthUserServer();
        server.start();
        server.blockUntilShutdown();
    }
    
    static class AuthUserImpl extends AuthUserGrpc.AuthUserImplBase {
        @Override
        public void createAuthUser(CreateAuthUserRequest req, StreamObserver<CreateAuthUserReply> responseObserver) {
            // FIXME, do something
            AuthUserReply rpl = AuthUserReply.newBuilder().setMsg("abc").build();
            CreateAuthUserReply reply = CreateAuthUserReply.newBuilder().setReply(rpl).build();
            responseObserver.onNext(reply);
            responseObserver.onCompleted();
        }

        @Override
        public void readAuthUser(ReadAuthUserRequest req, StreamObserver<ReadAuthUserReply> responseObserver) {
            // FIXME, do something
            AuthUserReply rpl = AuthUserReply.newBuilder().setMsg("abc").build();
            ReadAuthUserReply reply = ReadAuthUserReply.newBuilder().setReply(rpl).build();
            responseObserver.onNext(reply);
            responseObserver.onCompleted();
        }

        @Override
        public void updateAuthUser(UpdateAuthUserRequest req, StreamObserver<UpdateAuthUserReply> responseObserver) {
            // FIXME, do something
            AuthUserReply rpl = AuthUserReply.newBuilder().setMsg("abc").build();
            UpdateAuthUserReply reply = UpdateAuthUserReply.newBuilder().setReply(rpl).build();
            responseObserver.onNext(reply);
            responseObserver.onCompleted();
        }

        @Override
        public void deleteAuthUser(DeleteAuthUserRequest req, StreamObserver<DeleteAuthUserReply> responseObserver) {
            // FIXME, do something
            AuthUserReply rpl = AuthUserReply.newBuilder().setMsg("abc").build();
            DeleteAuthUserReply reply = DeleteAuthUserReply.newBuilder().setReply(rpl).build();
            responseObserver.onNext(reply);
            responseObserver.onCompleted();
        }
    }
}