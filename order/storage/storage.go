package storage

import (
	"context"
	pb "grpc-demo/order/proto"
)

// Storage ...
type Storage interface {
	SaveOrder(ctx context.Context, order *pb.Order) error
	GetOrder(ctx context.Context, orderID string) (*pb.Order, error)
	UpdateOrder(ctx context.Context, order *pb.Order) error
	DeleteOrder(ctx context.Context, orderID string) (*DeleteOrderResult, error)
}

type storageImpl struct {
	db    dbRepository
	cache cacheRepository
}

// New ...
func New(pgClient, redisClient string) Storage {
	return &storageImpl{
		db:    newDB(pgClient),
		cache: newCache(redisClient),
	}
}

func (s *storageImpl) SaveOrder(ctx context.Context, order *pb.Order) error {
	if err := s.db.SaveOrder(ctx, order); err != nil {
		return err
	}

	if err := s.cache.SetOrder(order); err != nil {
		return err
	}

	return nil
}

func (s *storageImpl) GetOrder(ctx context.Context, orderID string) (*pb.Order, error) {
	var order *pb.Order
	var err error

	order, err = s.cache.GetOrder(orderID)
	if err == nil {
		return order, nil
	}

	order, err = s.db.GetOrder(ctx, orderID)
	if err != nil {
		return nil, err
	}

	return order, nil
}

func (s *storageImpl) UpdateOrder(ctx context.Context, order *pb.Order) error {
	return s.db.UpdateOrder(ctx, order)
}

func (s *storageImpl) DeleteOrder(ctx context.Context, orderID string) (*DeleteOrderResult, error) {
	return s.db.DeleteOrder(ctx, orderID)
}
