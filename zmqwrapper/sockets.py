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
    _sock = None
    
    def __init__(self, address,socket_type):
        self._address = address
        self._ctx = zmq.Context()
        self._sock = self._ctx.socket(socket_type)
        self._sock.bind(address)               

    def sock(self):
        """
        Returns the zmq socket object being used for the connection. This can be used
        to send messages with additional flags etc.
        
            Returns:
                - The underlying zmq socket
        """
        return self._sock
        
    def close(self):
        """
        Close the socket connection.
        """
        self._sock.close()

class ClientConnection(object):
    """
    Creates a client side socket of given type.
    
        Args:
            - address: the address to use
            - socket_type: the tyoe of socket to open
    """

    _address = None
    _ctx = None
    _sock = None
    
    def __init__(self, address,socket_type):
        self._address = address
        self._ctx = zmq.Context()
        self._sock = self._ctx.socket(socket_type)
        self._sock.connect(address)               

    def sock(self):
        """
        Returns the zmq socket object being used for the connection. This can be used
        to receive messages with additional flags etc.
        
            Returns:
                - The underlying zmq socket
        """
        return self._sock

    def close(self):
        """
        Close the socket connection.
        """
        self._sock.close()        
