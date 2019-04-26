CURRENT_DIR=$(shell pwd)

DEV_IMAGE_NAME=order-service
DEV_CONTAINER_NAME=${DEV_IMAGE_NAME}

PROD_IMAGE_NAME=order-service
PROD_CONTAINER_NAME=${PROD_IMAGE_NAME}

CMD_ENTRYPOINT=${CURRENT_DIR}/cmd/main.go
SERVICE_NAME=order-service
DEV_PORT=1010:1010

proto:
	protoc -I /usr/local/include -I. \
			-I ${GOPATH}/src/github.com/gogo/protobuf/gogoproto \
			-I ${CURRENT_DIR}/proto/ \
      		--gofast_out=plugins=grpc:${CURRENT_DIR}/proto/ \
      		${CURRENT_DIR}/proto/*.proto

build-dev:
	CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o ${CURRENT_DIR}/bin/${SERVICE_NAME} ${CMD_ENTRYPOINT}
	docker build --rm -t ${DEV_IMAGE_NAME} .

run-dev:
	docker run --rm -p ${DEV_PORT} --name ${DEV_CONTAINER_NAME} ${DEV_IMAGE_NAME} -config=config/json/dev.json

.PHONY: proto