class Response:

    def __init__(self,request_headers,response_body):
        self.body = response_body

    def encode(self):
        return 'HTTP/1.1 200 OK\r\nServer: PyServer\r\n\r\n{}\r\n\r\n'.format(self.body).encode()


class DefaultResponseNotFound:

    def encode(self):
        return b'HTTP/1.1 404 Not Found\r\nServer: PyServer\r\n\r\n'

class DefaultResponseBadRequest:

    def encode(self):
        return b'HTTP/1.1 400 Not Found\r\nServer: PyServer\r\n\r\n'
