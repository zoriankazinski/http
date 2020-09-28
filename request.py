from utils import HttpCodes

class Header:

    _type = None
    _route = None

    legal_types = [ 
        "GET",
        "POST",
        "..."
    ]

    def __init__(self,request_header):
        lines = request_header.splitlines()
        self.Type = lines[0].split(' ')[0]
        self.Route = lines[0].split(' ')[1]
        self.Version = lines[0].split(' ')[2]
        for line in lines[1:-1]:
            key,value = line.split(': ')
            key = key.replace('-','__')
            setattr(self,key,value)

    def __getattr__(self,key):
        if key not in dir(self):
            return None
        return super().__getattr__(key)

    @property
    def Type(self):
        return self._type

    @Type.setter
    def Type(self,value):
        if value not in self.legal_types:
            raise Exception("Ilegal Request Type - No Such Type {}".format(value))
        self._type = value

    @property
    def Route(self):
        return self._route

    @Route.setter
    def Route(self,value):
        if not value.startswith('/'):
            raise Exception("Ilegal Route - has to start with / - {}".format(value))
        self._route = value

    @property
    def Version(self):
        return 'HTTP/1.1'

    @Version.setter
    def Version(self,value):
        if value != self.Version:
            raise Exception("Invalid Http Version! {}".format(value))

class Request:

    def __init__(self,request_text):
        self.Header = Header(request_text.split('\r\n\r\n')[0])
        self.Body = request_text.split('\r\n\r\n')[1]
