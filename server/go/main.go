package main

import (
	"fmt"
	"os"

	"server"
)

func main() {
	if len(os.Args) == 1 {
		s, err := server.NewAuthServer()
		if err != nil {
			fmt.Printf("Error when creating new gRPC service: %s", err.Error())
			return
		}
		fmt.Printf("Server booting up...\n")
		s.Init()
		s.Work()
	} else {
		fmt.Printf("DEBUGGING...\n")
	}

}
