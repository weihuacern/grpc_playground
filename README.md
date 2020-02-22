# gRPC Playground

In this repo, gRPC is used to implement the APIs for authentication and authorization server and client in multiple languages.

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
sudo apt install default-jre
sudo apt install default-jdk
sudo apt install maven
```

### NodeJS

```bash
sudo apt install nodejs
sudo apt install npm
sudo npm install -g grpc-tools
```

## Items

### Stage 1

- Golang gRPC server and client: Complete
- Python gRPC server and client: Complete
- Java gRPC server and client: Complete
- NodeJS gRPC server and client: Working
- An article to summary: Complete, [Link](https://weihuacern.github.io/2020/02/20/GRPC_BASIC_AND_EXAMPLES)

### Stage 2

- gRPC performance evaluation: Protobuf size, serialization and HTTP/2 stream.
- An article to summary

### Stage 3

- C++ gRPC server and client
- R language integration gRPC
- An article to summary
