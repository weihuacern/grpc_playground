PROTOMSGBASE := message
GOSERVERPATH := server/go
GOCLIENTPATH := client/go
PYTHONSERVERPATH := server/python
PYTHONCLIENTPATH := client/python
PYTHONOUTDIR := out
JAVASERVERPATH := server/java/server
JAVACLIENTPATH := client/java/client

all: prep rpc_go rpc_python rpc_java

## prep: Prepare for compile
prep:
	mkdir -p $(PROTOMSGBASE)/proto-go/src/message
	mkdir -p $(PROTOMSGBASE)/proto-python
	mkdir -p $(PYTHONOUTDIR)
	mkdir -p $(JAVASERVERPATH)/src/main/proto $(JAVASERVERPATH)/src/test/proto
	mkdir -p $(JAVACLIENTPATH)/src/main/proto $(JAVACLIENTPATH)/src/test/proto

## proto_go: Render protobuf messages into Golang files
proto_go:
	protoc -I=$(PROTOMSGBASE) --go_out=plugins=grpc:$(PROTOMSGBASE)/proto-go/src/message $(PROTOMSGBASE)/*.proto

## rpc_go: Build Golang gRPC server and client
rpc_go: proto_go
	make -C $(GOSERVERPATH)
	make -C $(GOCLIENTPATH)

## proto_python: Render protobuf messages into Python files
proto_python:
	python3 -m grpc_tools.protoc -I=$(PROTOMSGBASE) --python_out=$(PROTOMSGBASE)/proto-python --grpc_python_out=$(PROTOMSGBASE)/proto-python $(PROTOMSGBASE)/*.proto

## rpc_python: Build Python gRPC server and client
rpc_python: proto_python
	rm -rf $(PYTHONOUTDIR)/*
	pylint $(PYTHONSERVERPATH)/src/*
	cp -r $(PROTOMSGBASE)/proto-python/* $(PYTHONOUTDIR)/
	cp -r $(PYTHONSERVERPATH)/src/* $(PYTHONOUTDIR)/
	python3 -m zipapp $(PYTHONOUTDIR) -m "server:entry" -o  $(PYTHONSERVERPATH)/server.pyz
	rm -rf $(PYTHONOUTDIR)/*
	pylint $(PYTHONCLIENTPATH)/src/*
	cp -r $(PROTOMSGBASE)/proto-python/* $(PYTHONOUTDIR)/
	cp -r $(PYTHONCLIENTPATH)/src/* $(PYTHONOUTDIR)/
	python3 -m zipapp $(PYTHONOUTDIR) -m "client:entry" -o  $(PYTHONCLIENTPATH)/client.pyz
	rm -rf $(PYTHONOUTDIR)/*

## proto_java: Copy protobuf messages into Java repo, no render
proto_java:
	cp $(PROTOMSGBASE)/*.proto $(JAVASERVERPATH)/src/main/proto/
	cp $(PROTOMSGBASE)/*.proto $(JAVASERVERPATH)/src/test/proto/
	cp $(PROTOMSGBASE)/*.proto $(JAVACLIENTPATH)/src/main/proto/
	cp $(PROTOMSGBASE)/*.proto $(JAVACLIENTPATH)/src/test/proto/

## rpc_java: Build Java gRPC server and client
rpc_java: proto_java
	mvn -f $(JAVASERVERPATH)/pom.xml package
	mvn -f $(JAVACLIENTPATH)/pom.xml package

## clean: Clean up
clean:
	rm -rf $(PROTOMSGBASE)/proto-go
	rm -rf $(PROTOMSGBASE)/proto-python
	rm -rf $(PYTHONOUTDIR)
	rm -rf $(GOSERVERPATH)/server
	rm -rf $(GOCLIENTPATH)/client
	rm -rf $(PYTHONSERVERPATH)/server.pyz
	rm -rf $(PYTHONCLIENTPATH)/client.pyz
	rm -rf $(JAVASERVERPATH)/src/main/proto $(JAVASERVERPATH)/src/test/proto
	rm -rf $(JAVACLIENTPATH)/src/main/proto $(JAVACLIENTPATH)/src/test/proto
	mvn -f $(JAVASERVERPATH)/pom.xml clean
	mvn -f $(JAVACLIENTPATH)/pom.xml clean

## help: Obtain help related information
help: Makefile
	@sed -n 's/^##//p' $<
