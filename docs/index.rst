.. pyzmq-wrapper documentation master file, created by
   sphinx-quickstart on Thu Sep  5 07:44:15 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyzmq-wrapper's documentation!
=========================================

pyzmq-wrapper is a set of classes that provide wrappers over the zmq code - these aim to serve the 80%
cases where the developers just want to start a publisher or subscriber withut having to worry about
how the zmq connections are made or what flags are to be used for each message. The publishers and the
subscribers created by pyzmq-wrapper use the default values for all flags. The only assumption made is 
that the subscribers will be in non-blocking mode, so that you can use the subscriber in a thread and can 
shut it down easily. Also the subscriber provides a callback - freeing you from having to loop through
the receiving process.

The sock() method on the publishers and subscribers gives access to the underlying zmq socket object so that
you can use that for sending messages which require you to set certain flags.


Installation
------------

You can install this using

    pip install pyzmq-wrapper
    
    easy_install pyzmq-wrapper


Getting started
---------------


The following entities are provided to abstract the user from the zmq code.


Publisher
~~~~~~~~~

A simple pulisher can be started on a port as shown below. This object can then be used to send
messages - with or without a topic.

    from zmqwrapper import * 
    
    p=publisher('tcp://127.0.0.1:5555')
    p.publish("hello",RAW)
    #greeting is the topic
    p.publish("hello",MULTIPART,"greeting")
    
    
Subscriber
~~~~~~~~~~

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



API Docs:

.. toctree::
   :maxdepth: 4

   zmqwrapper


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

