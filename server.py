import socket
import select
import queue as Queue
from request import Request
from response import Response, DefaultResponse

class Server:
    
    inputs = []
    outputs = []
    messages = {}
    routes = {}

    donotkill = False

    def __init__(self,port=2145):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind(('',port))
        self.sock.listen(50)
        self.sock.setblocking(0)
        self.inputs.append(self.sock)

    def handle_new_connection(self):
        conn, addr = self.sock.accept()
        conn.setblocking(0)
        self.inputs.append(conn)
        self.messages[conn] = Queue.Queue()

    def handle_new_readable(self,conn):
        data = conn.recv(60000)
        if not data:
            return self.remove_connection(conn)
        request = Request(data.decode())
        self.messages[conn].put(self.answer(request))
        if conn not in self.outputs:
            self.outputs.append(conn)

    def remove_connection(self,conn):
        if conn in self.outputs:
            self.outputs.remove(conn)
        self.inputs.remove(conn)
        conn.close()
        del self.messages[conn]

    def handle_readables(self,conn):
        if conn is self.sock:
            self.handle_new_connection()
        else:
            self.handle_new_readable(conn)

    def handle_writeables(self,conn):
        try:
            msg = self.messages[conn].get_nowait()
        except Queue.Empty:
            self.outputs.remove(conn)
        else:
            conn.send(msg)
            self.remove_connection(conn)

    def handle_exceptionals(self,conn):
        self.remove_connection(conn)

    def __call__(self):
        while self.inputs:
            r,w,e = select.select(self.inputs,self.outputs,self.inputs)
            for s in r:
                self.handle_readables(s)
            for s in w:
                self.handle_writeables(s)
            for s in e:
                self.handle_execptionals(s)

    def add_route(self,route,function):
        self.routes[route] = function

    def answer(self,request):
        route = request.Header.Route
        if route not in self.routes:
            return DefaultResponse.NotFound()
        try:
            return Response(request.Header,self.routes[route](request.Body))
        except:
            return DefaultResponse.BadRequest()            

A = Server()
A.add_route('/',lambda x: None)
A()
