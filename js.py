"""
    A websocket <-> Server js code injector for live js evaluation
"""

class Element:

    def __init__(self,ID):
        self.el = 'document.getElementById("{}")'.format(ID)

    @property
    def innerHTML(self):
        return '{}.innerHTML'.format(self.el)


    @innerHTML.setter
    def innerHTML(self,value):
        return '{} = "{}"'.format(self.innerHTML,value)

class Script:
    
    @staticmethod
    def getElementById(element):
        return 'document.getElementById("{}")'.format(element)

