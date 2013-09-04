import zmq
from sockets import ServerConnection
from constants import *

def publisher(address):
    """
    Creates a publisher binding to the given port number.

        Args:
            address: the address to bind the PUB socket to.
    """
    return Publisher(address)
    
class Publisher(ServerConnection):
    """
    Publisher that can send messages to ZMQ
    
        Args:
            address: the address to bind to
    """

    def __init__(self,address):
        super(Publisher,self).__init__(address,zmq.PUB)
        
        
    def publish(self,message,message_type,topic=''):
        """
        Publish the message on the PUB socket without a topic name.
        
        Args:
            message: the message to publish
            message_type: the type of message being sent
        """
        if message_type == RAW:
            self._sock.send(message)
        elif message_type == PYOBJ:
            self._sock.send_pyobj(message)
        elif message_type == JSON:
            self._sock.send_json(message)
        elif message_type == MULTIPART:
            self._sock.send_multipart([topic, message])
        elif message_type == STRING:
            self._sock.send_string(message)
        elif message_type == UNICODE:
            self._sock.send_unicode(message)
        else:
            raise Exception("Unknown message type %s"%(message_type,))
