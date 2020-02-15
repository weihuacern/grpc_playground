GOPATH := /home/huawei/go:$(PWD):$(PWD)/client/go:$(PWD)/../../message/proto-go:$(PWD)/message/proto-go
GOBINARYNAME := client
export GOPATH

all: client

lint:
	golint

client: lint
	go build -o $(GOBINARYNAME)

clean:
	rm -rf $(GOBINARYNAME)

.PHONY: all client
