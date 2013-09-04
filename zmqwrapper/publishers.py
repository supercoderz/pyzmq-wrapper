import zmq

def json_publisher(port):
    """
    Creates a JSON publisher binding to the given port number.

        Args:
            port: the port to bind the PUB socket to.
    """
    return JsonPublisher(port)
    
class AbstractPublisher(object):
    """
    The Publisher class creates a PUB socket on the given port.
    Once created you can use this to publish messages on a 
    specific topic or without any topic.
    
        Args:
            port: the port to use
    """

    _port = None
    _ctx = None
    
    def __init__(self, port):
        self._port = port
        self._ctx = zmq.Context()
        self._sock = self._ctx.socket(zmq.PUB)
        self._sock.bind(port)
        
    def port(self):
        """
        Returns the port in use
        """
        return self._port
        

class JsonPublisher(AbstractPublisher):
    """
    Publisher that sends messages in json format
    """
    def publish(self,message):
        """
        Publish the message on the PUB socket without a topic name.
        
        Args:
            message: the message to publish
        """
        self._sock.send_json(message)
