from protos.book_service_pb2_grpc import BookServicer
from protos.book_service_pb2 import AuthorResponse


class BookService(BookServicer):
    def GetAuthor(self, request, context):
        return AuthorResponse(id=1, name='first author')
