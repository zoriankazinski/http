
class Response:

    def __new__(self,request_headers,response_body,**kwargs):
        self.body = response_body

        class RespBytes(bytes):

            def __new__(cls,*args,**kwargs):
                to_return = 'HTTP/1.1 200 OK\r\n\r\n{}\r\n\r\n'.format(self.body)
                return super().__new__(cls,to_return,encoding='utf-8')

        class EmptyRespBytes(bytes):

            def __new__(cls,*args,**kwargs):
                return super().__new__(cls,'HTTP/1.1 204 No Content\r\n\r\n',encoding='utf-8')

        if self.body:
            return RespBytes()

        return EmptyRespBytes()


class DefaultResponse:

    class BadRequest(bytes):

        def __new__(cls,*args,**kwargs):
            return super().__new__(cls,'HTTP/1.1 400 Bad Request\r\n\r\n',encoding='utf-8')

    class Unauthorized:

        def __new__(cls,*args,**kwargs):
            return super().__new__(cls,'HTTP/1.1 401 Unauthorized\r\n\r\n',encoding='utf-8')

    class Forbidden:

        def __new__(cls,*args,**kwargs):
            return super().__new__(cls,'HTTP/1.1 403 Forbidden\r\n\r\n',encoding='utf-8')

    class NotFound(bytes):

        def __new__(cls,*args,**kwargs):
            return super().__new__(cls,'HTTP/1.1 404 Not Found\r\n\r\n',encoding='utf-8')

    class Method_Not_Allowed(bytes):

        def __new__(cls,*args,**kwargs):
            return super().__new__(cls,'HTTP/1.1 405 Method Not Allowed\r\n\r\n',encoding='utf-8')

