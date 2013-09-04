pyzmq-wrapper
=============

<<<<<<< HEAD
A set of wrapper classes over pyzmq that provide a simper interface and additional functionality.

The following entities are provided to abstract the user from the zmq code.

Publisher
---------

A simple pulisher can be started on a port as shown below. This object can then be used to send
messages - with or without a topic.

    from zmqwrapper import publisher 
    p=publisher(5555)
    #just send hello without any topic
    p.publish("hello")
    #greeting is the topic
    p.publish("greeting","hello")
    
    
Subscriber
----------

A simple subscriber can be created by passing a port, a list of topics and a single callback. The callback is executed
for every message that is received on the topic.


    from zmqwrapper import subscriber
    #define the callback
    def process_greeting(greeting):
        print greeting
        
    
    #create the subscriber
    s=subscriber(5555,['greetings'],process_greeting)
    #and start it so that we can process the messages
    s.start()
    

MultiSubscriber
---------------

Similar to a subscriber but this takes a map of topics to callbacks.

    from zmqwrapper import subscriber
    #define the callback
    def process_greeting(greeting):
        print greeting
        
    from zmqwrapper import Subscriber
    #create the subscriber
    s=subscriber(5555,{'greetings':process_greeting},multi=True)
    #and start it so that we can process the messages
    s.start()

=======
A set of wrapper classes over pyzmq that provide a simper interface and additional functionality
>>>>>>> df7cb468c9244c1c82062526bcddbda823645348
