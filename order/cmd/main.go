package main

import (
	"flag"
	"log"
	"net"
	"os"
	"os/signal"
	"syscall"

	"grpc-demo/order/config"
	pb "grpc-demo/order/proto"
	"grpc-demo/order/service"
	"grpc-demo/order/storage"

	"google.golang.org/grpc"
)

const (
	prefix = "[order_srv]"
)

var (
	configPath = flag.String("config", "", "Config file path")
)

func main() {
	flag.Parse()

	// =========================================================================
	// Logging
	log := log.New(os.Stdout, prefix, log.LstdFlags|log.Lmicroseconds|log.Lshortfile)

	// =========================================================================
	// Config
	config, err := config.Load(*configPath)
	if err != nil {
		log.Fatal(err)
	}

	// =========================================================================
	// Storage
	storage := storage.New("postgresql-client", "redis-client")

	// =========================================================================
	// Service
	service := service.New(storage)

	// =========================================================================
	// GRPC Server
	lis, err := net.Listen("tcp", config.RPCPort)
	if err != nil {
		log.Fatalf("main: Net Listener : %v", err)
	}

	defer lis.Close()

	grpcServer := grpc.NewServer()
	pb.RegisterOrderServiceServer(grpcServer, service)

	log.Println("main: Listeninig gRPC Service")
	log.Printf(" - port:%v", config.RPCPort)

	serverError := make(chan error, 1)

	// Start the service listening the request
	go func() {
		serverError <- grpcServer.Serve(lis)
	}()

	// =========================================================================
	// Shutdown

	// Make a channel to listen for an interrupt or terminate signal from the OS.
	// Use a buffered channel because the signal package requires it.
	osSignals := make(chan os.Signal, 1)
	signal.Notify(osSignals, os.Interrupt, syscall.SIGTERM)

	// =========================================================================
	// Stop API Service

	// Blocking main and waiting for shutdown.
	select {
	case err := <-serverError:
		log.Fatalf("main : Error starting server: %v", err)

	case <-osSignals:
		log.Println("main : Start shutdown...")
		grpcServer.GracefulStop()
		return
	}
}
