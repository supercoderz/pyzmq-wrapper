from requestors import requestor
from repliers import replier
from constants import *
import time

def test_init_requestor():
    def foo(message,requestor):
        pass
    rq=requestor('tcp://127.0.0.1:5555',foo,JSON)
    assert rq is not None
    assert rq.sock() is not None
    rq.close()
    
def test_init_replier():
    def foo(message,requestor):
        pass
    rq=requestor('tcp://127.0.0.1:5555',foo,JSON)
    rp=replier('tcp://127.0.0.1:5555',foo,JSON)
    assert rq is not None
    assert rq.sock() is not None
    assert rp is not None
    assert rp.sock() is not None
    rq.close()
    rp.close()    
    
def test_init_basic_reqrep():
    def foo(message,requestor):
        assert message == 'test message'
    def foo1(message,replier):
        assert message == 'test message'
        replier.reply(message,JSON)
    rq=requestor('tcp://127.0.0.1:5555',foo,JSON)
    rp=replier('tcp://127.0.0.1:5555',foo1,JSON)
    rq.start()
    rp.start()
    assert rq is not None
    assert rq.sock() is not None
    assert rp is not None
    assert rp.sock() is not None
    rq.request('test message',JSON)
    time.sleep(2)
    rq.stop()
    rp.stop()
    time.sleep(2)
    rq.close()
    rp.close()
