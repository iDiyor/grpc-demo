package service

import (
	"context"
	pb "grpc-demo/order/proto"
	storage "grpc-demo/order/storage"
	"time"
)

// Service ...
type Service struct {
	storage storage.Storage
}

// New ...
func New(storage storage.Storage) *Service {
	return &Service{
		storage: storage,
	}
}

// CreateOrder creates an order, saves in db and publishes an event
func (s *Service) CreateOrder(ctx context.Context, req *pb.CreateOrderRequest) (*pb.Order, error) {
	order := pb.Order{
		Id:              "12345",
		CarrierId:       req.GetCarrierId(),
		CarrierName:     req.GetCarrierName(),
		CarrierContact:  req.GetCarrierContact(),
		PickupAddress:   req.GetPickupAddress(),
		DeliveryAddress: req.GetDeliveryAddress(),
		Price:           req.GetPrice(),
		Timestamp:       time.Now().UTC().Format(time.RFC3339),
	}

	if err := s.storage.SaveOrder(ctx, &order); err != nil {
		return nil, err
	}

	return &order, nil
}

// GetOrder does magic
func (s *Service) GetOrder(ctx context.Context, req *pb.GetOrderRequest) (*pb.Order, error) {
	order, err := s.storage.GetOrder(ctx, req.GetOrderId())
	if err != nil {
		return nil, err
	}

	return order, nil
}

// UpdateOrder does another magic
func (s *Service) UpdateOrder(ctx context.Context, req *pb.Order) (*pb.EmptyResponse, error) {
	if err := s.storage.UpdateOrder(ctx, req); err != nil {
		return nil, err
	}

	return &pb.EmptyResponse{}, nil
}

// DeleteOrder does another brilliant magic
func (s *Service) DeleteOrder(ctx context.Context, req *pb.DeleteOrderRequest) (*pb.DeleteOrderResponse, error) {
	result, err := s.storage.DeleteOrder(ctx, req.GetOrderId())
	if err != nil {
		return nil, err
	}

	return &pb.DeleteOrderResponse{
		Someeventfields: result.CarrierID,
	}, nil
}
