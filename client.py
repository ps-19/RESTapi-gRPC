import grpc
import calculator_pb2
import calculator_pb2_grpc
from urllib import response

channel=grpc.insecure_channel('localhost:3000')
stub=calculator_pb2_grpc.YourServiceStub(channel)
ans=calculator_pb2.Number(value=100, value2=100)
response=stub.Sum(ans)
print(response.value)
