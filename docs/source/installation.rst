Installation
============

plico is tested on Python 2.7/3.6+ on ubuntu, mac, windows. 

It depends on zmq, numpy and pyfits (to store calibrations). You need a backend (PyQt4/PySide, PyQt5/PySide2) for GUIs.

It is not very useful to install this package by itself. See `plico-tipico <https://tipico.readthedocs.io/>`_ to install an example applications simulating some HW controller and a corresponding client. 

Anyhow, if you really want to install plico as standalone package go on with pip::

  pip install plico
