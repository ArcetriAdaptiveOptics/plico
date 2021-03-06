# PLICO: Python Laboratory Instrumentation COntrol

 [![Build Status][travis]][travislink]  [![Coverage Status][coveralls]][coverallslink] [![Documentation Status](https://readthedocs.org/projects/plico/badge/?version=latest)](https://plico.readthedocs.io/en/latest/?badge=latest) [![PyPI version][pypiversion]][pypiversionlink]


plico is a framework to develop applications controlling instrumentation typically available in a scientific laboratory.
It is entirely written in Python and support server-client applications, using [zeromq][zmq] as message dispatcher.



A list of packages using plico:
   1. [tipico][tipico] and [tipico-server][tipico-server] implements a useless hardware-less typical application controlling a simulated instrument
   1. [pysilico][pysilico] and [pysilico-server][pysilico-server] to control videocameras.
   1. [palpao][palpao] and [palpao-server][palpao-server] to control deformable mirrors


## Documentation

https://plico.readthedocs.io




## Installation

plico runs on Python 2.7+ and Python 3.3+. 

It depends on zmq, numpy and pyfits (to store calibrations). You need a backend (PyQt4/PySide, PyQt5/PySide2) for GUIs.

It is not very useful to install this package by itself. See [tipico][tipico] to install an example applications simulating some HW controller and a corresponding client. 

Anyhow, if you really want to install plico as standalone package go on with pip:

```
pip install plico
```

## Documentation
Visit the wiki for the projects https://github.com/lbusoni/plico/wiki




[zmq]: http://zeromq.org
[plico]: https://github.com/ArcetriAdaptiveOptics/plico
[tipico]: https://github.com/ArcetriAdaptiveOptics/tipico
[tipico-server]: https://github.com/ArcetriAdaptiveOptics/tipico_server
[pysilico]: https://github.com/ArcetriAdaptiveOptics/pysilico
[pysilico-server]: https://github.com/ArcetriAdaptiveOptics/pysilico_server
[travis]: https://travis-ci.com/ArcetriAdaptiveOptics/palpao.svg?branch=master "go to travis"
[travislink]: https://travis-ci.com/ArcetriAdaptiveOptics/plico
[coveralls]: https://coveralls.io/repos/github/ArcetriAdaptiveOptics/plico/badge.svg?branch=master "go to coveralls"
[coverallslink]: https://coveralls.io/github/ArcetriAdaptiveOptics/plico
[pypiversion]: https://badge.fury.io/py/plico.svg
[pypiversionlink]: https://badge.fury.io/py/plico

