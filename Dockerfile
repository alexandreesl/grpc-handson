FROM grpc/python:1.0-onbuild
CMD [ "python", "./gRPC_server.py" ]