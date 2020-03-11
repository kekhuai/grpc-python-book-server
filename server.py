import grpc
from concurrent import futures
from protos import book_service_pb2_grpc
from grpc_python_book_server import book_service


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_service_pb2_grpc.add_BookServicer_to_server(
        book_service.BookService(),
        server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if '__main__' == __name__:
    serve()
