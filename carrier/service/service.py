
import grpc
from ..proto import service_pb2_grpc
from ..storage import Storage

class CarrierService(service_pb2_grpc.CarrierServiceServicer):
    name = "carrier_service"
    def __init__(self, storage: Storage):
        self.storage = storage

    def CreateCarrier(self, request, context):
        # create carrier
        # storage operations
        # publish event
        # other logic
        # return

