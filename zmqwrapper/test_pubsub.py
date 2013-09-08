from publishers import publisher
from subscribers import subscriber
from constants import *
import time

def test_init_publisher():
    p=publisher('tcp://127.0.0.1:5555')
    assert p is not None
    assert p.sock() is not None
    p.close()
    
def test_init_subscriber():
    p=publisher('tcp://127.0.0.1:5555')
    def foo(topic, message):
        pass
    s=subscriber('tcp://127.0.0.1:5555',[''],foo,JSON)
    assert p is not None
    assert p.sock() is not None
    assert s is not None
    assert s.sock() is not None
    p.close()
    s.close()    
    
def test_init_basic_subscribe():
    p=publisher('tcp://127.0.0.1:5555')
    def foo(topic, message):
        assert message == 'test message'
    s=subscriber('tcp://127.0.0.1:5555',['test'],foo,STRING)
    s.start()
    assert p is not None
    assert p.sock() is not None
    assert s is not None
    assert s.sock() is not None
    p.publish('test message',STRING,'test')
    time.sleep(2)    
    s.stop()
    s.close()        
    p.close()

