# gRPC Playground

In this repo, gRPC is used to design the API for authentication and authorization server and client in multiple languages.

## Dependencies

### Golang
```bash
go get -u golang.org/x/lint/golint
go get -u github.com/golang/protobuf/protoc-gen-go
go get -u google.golang.org/grpc
```

### Python
```bash
pip3 install pylint==2.4.4
pip3 install grpcio
pip3 install grpcio-tools
```

### Java
```bash
mvn -B archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DgroupId=com.example.grpc -DartifactId=server
mvn -B archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DgroupId=com.example.grpc -DartifactId=client
```

## Items

### Stage 1
- Golang gRPC server and client: Complete
- Python gRPC server and client: Complete
- Java gRPC server and client: Working
- NodeJS gRPC server and client: Working
- An article to summary: Working

### Stage 2
- C++ gRPC server and client
- R language integration gRPC
