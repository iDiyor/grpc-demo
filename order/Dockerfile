FROM alpine:latest  
RUN apk --no-cache add ca-certificates
RUN apk add --update tzdata
COPY ./config /go/src/order/config
COPY ./bin/order-service /go/bin/order-service
WORKDIR /go/src/order
ENTRYPOINT ["/go/bin/order-service"] 

EXPOSE 1010