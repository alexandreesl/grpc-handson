import random
import time

import grpc

import my_service_pb2 as my_service_pb2
import my_service_pb2_grpc as my_service_pb2_grpc


class gRPCClient():
    def __init__(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = my_service_pb2_grpc.MyServiceStub(channel)

    def method1(self, name, code):
        print('method 1')
        return self.stub.MyMethod1(my_service_pb2.MyRequest(name=name, code=code))

    def method2(self, name, code):
        print('method 2')
        return self.stub.MyMethod2(my_service_pb2.MyRequest(name=name, code=code))

    def method3(self, req):
        print('method 3')
        return self.stub.MyMethod3(req)


def generateRequests():
    reqs = [my_service_pb2.MyRequest(name='Alexandre', code=123), my_service_pb2.MyRequest(name='Maria', code=123),
            my_service_pb2.MyRequest(name='Eleuterio', code=123), my_service_pb2.MyRequest(name='Lucebiane', code=123),
            my_service_pb2.MyRequest(name='Ana Carolina', code=123)]

    for req in reqs:
        yield req
        time.sleep(random.uniform(2, 4))


def main():
    print('main')

    client = gRPCClient()

    print(client.method1('Alexandre', 123))
    print(client.method2('Maria', 123))

    res = client.method3(generateRequests())

    for re in res:
        print(re)


if __name__ == '__main__':
    main()
