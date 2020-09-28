class Response:

    def __init__(self,request_headers,response_body):
        self.body = response_body

    def encode(self):
        return 'HTTP/1.1 200 OK\r\nServer: PyServer\r\n\r\n{}\r\n\r\n'.format(self.body).encode()


class DefaultResponse:

    class BadRequest(bytes):

        def __new__(cls,*args,**kwargs):
            return super().__new__(cls,'HTTP/1.1 400 Not Found\r\n\r\n',encoding='utf-8')

    class Unauthorized:

        def __new__(cls,*args,**kwargs):
            return super().__new__(cls,'HTTP/1.1 401 Unauthorized\r\n\r\n',encoding='utf-8')

    class NotFound(bytes):

        def __new__(cls,*args,**kwargs):
            return super().__new__(cls,'HTTP/1.1 404 Not Found\r\n\r\n',encoding='utf-8')


