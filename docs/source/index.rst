PLICO: Python Laboratory Instrumentation COntrol
================================================

plico is a framework to develop applications that control instrumentation typically available in a scientific optics laboratory.
It is entirely written in Python and support server-client applications, using `zeromq <http://zeromq.org/>`_ as message dispatcher.


Supported instrumentation
=========================

The following is the list of avialable packages based on plico:

1. `plico-tipico <https://tipico.readthedocs.io/>`_ and `plico-tipico-server <https://tipico.readthedocs.io/>`_ implements a useless hardware-less typical application controlling a simulated instrument
2. `plico-camera <https://pysilico.readthedocs.io/>`_ and `plico-camera-server <https://pysilico.readthedocs.io/>`_  to control videocameras.
3. `plico-dm <https://palpao.readthedocs.io/>`_ and `plico-dm-server <https://palpao.readthedocs.io/>`_  to control deformable mirrors




Table of Contents
^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2
   
   api
   modules
   license
   help
   
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
