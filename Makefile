PROTOMSGBASE := message
GOSERVERPATH := server/go
GOCLIENTPATH := client/go

all: prep rpc_go

## prep: Prepare for compile
prep:
	mkdir -p $(PROTOMSGBASE)/proto-go/src/message

## proto_go: Render protobuf messages into golang files
proto_go:
	protoc -I=$(PROTOMSGBASE) --go_out=plugins=grpc:$(PROTOMSGBASE)/proto-go/src/message $(PROTOMSGBASE)/*.proto

## rpc_go: Build Golang gRPC server and client
rpc_go: proto_go
	make -C $(GOSERVERPATH)
	make -C $(GOCLIENTPATH)

## clean: Clean up
clean:
	rm -rf $(PROTOMSGBASE)/proto-go
	rm -rf $(GOSERVERPATH)/server
	rm -rf $(GOCLIENTPATH)/client

## help: Obtain help related information
help: Makefile
	@sed -n 's/^##//p' $<
