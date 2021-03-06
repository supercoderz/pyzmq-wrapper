from .producers import producer
from .consumers import consumer
from .constants import *
import time
import threading
from flaky import flaky

@flaky(max_runs=5)
def test_init_producer():
    p=producer('ipc:///tmp/test/0')
    assert p is not None
    assert p.sock() is not None
    p.close()
    
@flaky(max_runs=5)
def test_init_consumer():
    p=producer('ipc:///tmp/test/0')
    def foo(message):
        pass
    c=consumer('ipc:///tmp/test/0',foo,JSON)
    assert p is not None
    assert p.sock() is not None
    assert c is not None
    assert c.sock() is not None
    p.close()
    c.close()    
    
@flaky(max_runs=5)
def test_init_basic_consume():
    m = threading.Condition()
    m.acquire()
    p=producer('ipc:///tmp/test/0')
    def foo(message):
        m.acquire()
        assert message == u'test message'
        m.notifyAll()
        m.release()
    c=consumer('ipc:///tmp/test/0',foo,STRING)
    c.start()
    assert p is not None
    assert p.sock() is not None
    assert c is not None
    assert c.sock() is not None
    p.push(u'test message',STRING)
    m.wait() 
    m.release()
    c.stop()   
    c.close()        
    p.close()

