# PLICO: Python Laboratory Instrumentation COntrol

plico is a framework to develop applications controlling instrumentation typically available in a scientific laboratory.
It is entirely written in Python and support server-client applications, using [zeromq][zmq] as message dispatcher.



[zmq]: http://zeromq.org


## Installation

It is not very useful to install this package by itself. See [tipico][tipico] to install an example applications simulating some HW controller and a corresponding client. 

Anyhow, if you really want to install plico as standalone package go on with pip:

```
pip install plico
```

## Wish list

   + Documentation (readthedocs or alike)
   + Implement reconnect-to-devices in case of lost connection
   + Implement service discovery 


[tipico]: https://github.com/lbusoni/tipico
