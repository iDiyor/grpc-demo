CURRENT_DIR=$(shell pwd)

proto:
	python -m grpc_tools.protoc -I ${CURRENT_DIR}/proto \
			--python_out=${CURRENT_DIR}/proto \
			--grpc_python_out=${CURRENT_DIR}/proto \
			 ${CURRENT_DIR}/proto/*.proto

proto-go:
	protoc -I /usr/local/include -I. \
			-I ${GOPATH}/src/github.com/gogo/protobuf/gogoproto \
			-I ${CURRENT_DIR}/proto/ \
      		--gofast_out=plugins=grpc:${CURRENT_DIR}/proto/ \
      		${CURRENT_DIR}/proto/*.proto

.PHONY: proto