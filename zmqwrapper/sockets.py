import zmq

class ServerConnection(object):
    """
    Creates a server side socket of given type.
    
        Args:
            - address: the address to use
            - socket_type: the tyoe of socket to open
    """

    _address = None
    _ctx = None
    
    def __init__(self, address,socket_type):
        self._address = address
        self._ctx = zmq.Context()
        self._sock = self._ctx.socket(socket_type)
        self._sock.bind(address)               


class ClientConnection(object):
    """
    Creates a client side socket of given type.
    
        Args:
            - address: the address to use
            - socket_type: the tyoe of socket to open
    """

    _address = None
    _ctx = None
    
    def __init__(self, address,socket_type):
        self._address = address
        self._ctx = zmq.Context()
        self._sock = self._ctx.socket(socket_type)
        self._sock.connect(address)               

