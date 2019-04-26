package storage

import (
	"context"
	pb "grpc-demo/order/proto"
)

type dbRepository interface {
	SaveOrder(ctx context.Context, order *pb.Order) error
	GetOrder(ctx context.Context, orderID string) (*pb.Order, error)
	UpdateOrder(ctx context.Context, order *pb.Order) error
	DeleteOrder(ctx context.Context, orderID string) (*DeleteOrderResult, error)
}

type pgRepositoryImpl struct {
	pgClient string
}

func newDB(pgClient string) dbRepository {
	return &pgRepositoryImpl{
		pgClient: pgClient,
	}
}

func (r *pgRepositoryImpl) SaveOrder(ctx context.Context, order *pb.Order) error {
	// db queries and exec
	return nil
}

func (r *pgRepositoryImpl) GetOrder(ctx context.Context, orderID string) (*pb.Order, error) {
	return nil, nil
}

func (r *pgRepositoryImpl) UpdateOrder(ctx context.Context, order *pb.Order) error {
	return nil
}

func (r *pgRepositoryImpl) DeleteOrder(ctx context.Context, orderID string) (*DeleteOrderResult, error) {
	return nil, nil
}
