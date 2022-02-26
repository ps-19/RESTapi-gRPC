import time
import grpc
import calculator_pb2
import calculator_pb2_grpc
from concurrent import futures

class CalculatorServicer(calculator_pb2_grpc.YourServiceServicer):
    def Sum(self, request, context):
        res=calculator_pb2.Number()
        res.value=request.value+request.value2
        return res

def run():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    calculator_pb2_grpc.add_YourServiceServicer_to_server(CalculatorServicer(),server)
    print('Server Running On Port 3000')
    server.add_insecure_port('[::]:3000')
    server.start()
    SECOND=10
    try:
        while True:
            time.sleep(SECOND)
    except KeyboardInterrupt:
        server.stop(0)

if __name__=='__main__':
    run()