GOPATH := /home/huawei/go:$(PWD):$(PWD)/server/go:$(PWD)/../../message/proto-go:$(PWD)/message/proto-go
GOBINARYNAME := server
export GOPATH

all: server

lint:
	golint

server: lint
	go build -o $(GOBINARYNAME)

clean:
	rm -rf $(GOBINARYNAME)

.PHONY: all server
