package storage

import pb "grpc-demo/order/proto"

type cacheRepository interface {
	SetOrder(order *pb.Order) error
	GetOrder(orderID string) (*pb.Order, error)
}

type redisRepositoryImpl struct {
	redisClient string
}

// newCache ...
func newCache(redisClient string) cacheRepository {
	return &redisRepositoryImpl{
		redisClient: redisClient,
	}
}

func (r *redisRepositoryImpl) SetOrder(order *pb.Order) error {
	return nil
}

func (r *redisRepositoryImpl) GetOrder(orderID string) (*pb.Order, error) {
	return nil, nil
}
