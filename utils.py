#!/bin/python3
"""
    Python Request Data Type Module
"""
from enum import Enum

class HttpCodes(Enum):
    
    def __str__(self):
        """
            Print in the Http Response/Request Structure:
                Code Name
                200 Ok
        """
        return '{} {}'.format(self.value, self.name)
    
    @property
    def name(self):
        """
            Return the name property in a string format and not a var format
        """
        return super().name.replace('__',' ').replace('_','-')
    
    # Information
    Continue = 100
    Switching_Protocols = 101
    # Sucsessful
    OK = 200
    Created = 201
    Accepted = 202
    Non_Authorative__Information = 203
    No__Content = 204
    Reset__Content = 205
    Partial__Content = 206
    # Redirection
    Multiple__Choices = 300
    Moved__Permanently = 301
    Found = 302
    See__Other = 303
    Not__Modified = 304
    Use__Proxy = 305
    Unused = 306
    Temporary__Redirect = 307
    # Client Error
    Bad__Request = 400
    Unauthorized = 401
    Payment__Required = 402
    Forbidden = 403
    Not__Found = 404
    Method__Not__Allowed = 405
    Not__Acceptable = 406
    Proxy__Authentication__Required = 407
    Request__Timeout = 408
    Confilct = 409
    Gone = 410
    Length__Required = 411
    Precondition__Failed = 412
    Request__Entity__Too__Large = 413
    Request_url__Too__Long = 414
    Unsupported__Media__Type = 415
    Requested__Range__Not__Satisfiable = 416
    Expectation__Failed = 417
    # Server Error
    Internal__Server__Error = 500
    Not__Implemented = 501
    Bad__Gateway = 502
    Service__Unavailable = 503
    Gateway__Timeout = 504
    HTTP__Version__Not__Supported = 505
