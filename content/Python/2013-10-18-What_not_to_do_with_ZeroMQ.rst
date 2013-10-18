What not to do with ZeroMQ
##########################

`ZeroMQ`_ is a great networking library, and the `PyZMQ`_ package makes that
greatness accessible from Python. This week however, I encountered an
implementation pattern that is incompatible with ZeroMQ.

For *"reasons"*, I had wanted to use ZeroMQ inside a process in a way that was
blind to `process forks`_. Unfortunately, if a child interacts with a ZeroMQ
context inherited from its parent in anyway, including attempting to close it,
ZeroMQ will likely terminate with an `assertion failure`_. Compounding this,
not being able to close the context means leaking `file descriptors`_. The
worst case scenario is a child that does some work then forks, the parent exits
while the child repeats the sequence.

Here is a silly example that exercises a worst case.

.. code:: python

   import os
   import sys
   import zmq

   ADDRESS = 'tcp://127.0.0.1:5555'
   MAX_FORKS = 4096

   # the original parent creates a zeromq context and socket
   ctx = zmq.Context()
   sock = ctx.socket(zmq.PULL)
   sock.bind(ADDRESS)

   forked = 0
   if os.fork() != 0:
       # this parent listens for messages from its children
       while forked < MAX_FORKS:
           forked = sock.recv_json()
           sys.stdout.write('.')
           sys.stdout.flush()
       sys.exit(0)
   else:
       # the children discard the parent's context,
       # open a zeromq socket and send a message
       # to the first parent
       while forked < MAX_FORKS:
           forked += 1
           del ctx, sock
           ctx = zmq.Context()
           sock = ctx.socket(zmq.PUSH)
           sock.connect(ADDRESS)
           sock.send_json(forked)
           # after send a message, this child exits
           # spawning a new child to send a new message
           if os.fork() != 0:
               sys.exit(0)

Honestly this is a terrible design when using ZeroMQ. As evidenced by its
inevitable failure from running out of file descriptors. Sadly, I also have a
valid reason for wanting to be robust with this design. So my choices include:

1. Do not support network in children. (A valid but regrettable limitation)
2. Apply a different networking solution. (`Yak shaving`_)

Even if an `atfork`_ module that mirrored the existing `atexit`_ was added to
Python, it may not resolve this issue for me. The proposed atfork
implementation is Python only. When using CPython it would be oblivious to any
forks from inside C extensions.

ZeroMQ is still great. It's just not intended to work in this situation.

.. _ZeroMQ: http://zeromq.org/
.. _PyZMQ: https://pypi.python.org/pypi/pyzmq/13.1.0
.. _process forks: https://en.wikipedia.org/wiki/Fork_(system_call)
.. _assertion failure: http://www.mail-archive.com/zeromq-dev@lists.zeromq.org/msg19970.html
.. _file descriptors: https://en.wikipedia.org/wiki/File_descriptor
.. _Yak shaving: https://en.wiktionary.org/wiki/yak_shaving
.. _atfork: http://bugs.python.org/issue16500
.. _atexit: http://docs.python.org/dev/library/atexit.html
