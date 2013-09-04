pyzmq-wrapper
=============

A set of wrapper classes over pyzmq that provide a simper interface and additional functionality.

The following entities are provided to abstract the user from the zmq code.

Publisher
---------

A simple pulisher can be started on a port as shown below. This object can then be used to send
messages - with or without a topic.

    from zmqwrapper import * 
    
    p=publisher('tcp://127.0.0.1:5555')
    p.publish("hello",RAW)
    #greeting is the topic
    p.publish("hello",MULTIPART,"greeting")
    
    
Subscriber
----------

A simple subscriber can be created by passing a port, a list of topics and a single callback. The callback is executed
for every message that is received on the topic.


    from zmqwrapper import *
    
    #define the callback
    def process_greeting(topic,message):
        print message
        
    
    #create the subscriber
    s=subscriber('tcp://127.0.0.1:5555',['greetings'],process_greeting,MULTIPART)
    #and start it so that we can process the messages
    s.start()
    
