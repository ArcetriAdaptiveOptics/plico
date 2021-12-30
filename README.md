# PLICO: Python Laboratory Instrumentation COntrol

 ![Python package](https://github.com/ArcetriAdaptiveOptics/plico/workflows/Python%20package/badge.svg)
 [![codecov](https://codecov.io/gh/ArcetriAdaptiveOptics/plico/branch/master/graph/badge.svg?token=04PRSBMW11)](https://codecov.io/gh/ArcetriAdaptiveOptics/plico)
 [![Documentation Status](https://readthedocs.org/projects/plico/badge/?version=latest)](https://plico.readthedocs.io/en/latest/?badge=latest)
 [![PyPI version][pypiversion]][pypiversionlink]



plico is a framework to develop applications controlling instrumentation typically available in a scientific laboratory.
It is entirely written in Python and support server-client applications, using [zeromq][zmq] as message dispatcher.


## Documentation

https://plico.readthedocs.io

## Status of related packages
| | | | | | 
 --- | --- | --- | --- | --- 
[plico_motor](https://github.com/ArcetriAdaptiveOptics/plico_motor) | ![Python package](https://github.com/ArcetriAdaptiveOptics/plico_motor/workflows/Python%20package/badge.svg) | [![codecov](https://codecov.io/gh/ArcetriAdaptiveOptics/plico_motor/branch/main/graph/badge.svg?token=ApWOrs49uw)](https://codecov.io/gh/ArcetriAdaptiveOptics/plico_motor) | [![Documentation Status](https://readthedocs.org/projects/plico_motor/badge/?version=latest)](https://plico_motor.readthedocs.io/en/latest/?badge=latest) | [![PyPI version](https://badge.fury.io/py/plico-motor.svg)](https://badge.fury.io/py/plico-motor) 
[plico_motor_server](https://github.com/ArcetriAdaptiveOptics/plico_motor_server) | ![Python package](https://github.com/ArcetriAdaptiveOptics/plico_motor_server/workflows/Python%20package/badge.svg) | [![codecov](https://codecov.io/gh/ArcetriAdaptiveOptics/plico_motor_server/branch/main/graph/badge.svg?token=ApWOrs49uw)](https://codecov.io/gh/ArcetriAdaptiveOptics/plico_motor_server) |  [![Documentation Status](https://readthedocs.org/projects/plico_motor_server/badge/?version=latest)](https://plico_motor_server.readthedocs.io/en/latest/?badge=latest) | [![PyPI version](https://badge.fury.io/py/plico-motor-server.svg)](https://badge.fury.io/py/plico-motor-server) |
[pysilico](https://github.com/ArcetriAdaptiveOptics/pysilico) | ![Python package](https://github.com/ArcetriAdaptiveOptics/pysilico/workflows/Python%20package/badge.svg) | [![codecov](https://codecov.io/gh/ArcetriAdaptiveOptics/pysilico/branch/master/graph/badge.svg?token=GTDOW6IWDE)](https://codecov.io/gh/ArcetriAdaptiveOptics/pysilico) | [![Documentation Status](https://readthedocs.org/projects/pysilico/badge/?version=latest)](https://pysilico.readthedocs.io/en/latest/?badge=latest) | [![PyPI version](https://badge.fury.io/py/pysilico.svg)](https://badge.fury.io/py/pysilico)
[pysilico_server](https://github.com/ArcetriAdaptiveOptics/pysilico_server) | ![Python package](https://github.com/ArcetriAdaptiveOptics/pysilico_server/workflows/Python%20package/badge.svg) | [![codecov](https://codecov.io/gh/ArcetriAdaptiveOptics/pysilico_server/branch/master/graph/badge.svg?token=04PRSBMW11)](https://codecov.io/gh/ArcetriAdaptiveOptics/pysilico_server) | [![Documentation Status](https://readthedocs.org/projects/pysilico_server/badge/?version=latest)](https://pysilico_server.readthedocs.io/en/latest/?badge=latest) | [![PyPI version](https://badge.fury.io/py/pysilico-server.svg)](https://badge.fury.io/py/pysilico-server)
[palpao](https://github.com/ArcetriAdaptiveOptics/palpao) | ![Python package](https://github.com/ArcetriAdaptiveOptics/palpao/workflows/Python%20package/badge.svg) | [![codecov](https://codecov.io/gh/ArcetriAdaptiveOptics/palpao/branch/main/graph/badge.svg?token=ApWOrs49uw)](https://codecov.io/gh/ArcetriAdaptiveOptics/palpao) | [![Documentation Status](https://readthedocs.org/projects/palpao/badge/?version=latest)](https://palpao.readthedocs.io/en/latest/?badge=latest) | [![PyPI version](https://badge.fury.io/py/palpao.svg)](https://badge.fury.io/py/palpao)
[palpao_server](https://github.com/ArcetriAdaptiveOptics/palpao_server) | ![Python package](https://github.com/ArcetriAdaptiveOptics/palpao_server/workflows/Python%20package/badge.svg) | [![codecov](https://codecov.io/gh/ArcetriAdaptiveOptics/palpao_server/branch/main/graph/badge.svg?token=ApWOrs49uw)](https://codecov.io/gh/ArcetriAdaptiveOptics/palpao_server) | [![Documentation Status](https://readthedocs.org/projects/palpao_server/badge/?version=latest)](https://palpao_server.readthedocs.io/en/latest/?badge=latest) | [![PyPI version](https://badge.fury.io/py/palpao-server.svg)](https://badge.fury.io/py/palpao-server)
[plico_interferometer](https://github.com/ArcetriAdaptiveOptics/plico_interferometer) | ![Python package](https://github.com/ArcetriAdaptiveOptics/plico_interferometer/workflows/Python%20package/badge.svg) | [![codecov](https://codecov.io/gh/ArcetriAdaptiveOptics/plico_interferometer/branch/main/graph/badge.svg?token=ApWOrs49uw)](https://codecov.io/gh/ArcetriAdaptiveOptics/plico_interferometer) | [![Documentation Status](https://readthedocs.org/projects/plico_interferometer/badge/?version=latest)](https://plico_interferometer.readthedocs.io/en/latest/?badge=latest) | [![PyPI version](https://badge.fury.io/py/plico-interferometer.svg)](https://badge.fury.io/py/plico-interferometer)
[plico_interferometer_server](https://github.com/ArcetriAdaptiveOptics/plico_interferometer_server) | ![Python package](https://github.com/ArcetriAdaptiveOptics/plico_interferometer_server/workflows/Python%20package/badge.svg) | [![codecov](https://codecov.io/gh/ArcetriAdaptiveOptics/plico_interferometer_server/branch/main/graph/badge.svg?token=ApWOrs49uw)](https://codecov.io/gh/ArcetriAdaptiveOptics/plico_interferometer_server) | [![Documentation Status](https://readthedocs.org/projects/plico_interferometer_server/badge/?version=latest)](https://plico_interferometer_server.readthedocs.io/en/latest/?badge=latest) | [![PyPI version](https://badge.fury.io/py/plico-interferometer-server.svg)](https://badge.fury.io/py/plico-interferometer-server)
[tipico](https://github.com/ArcetriAdaptiveOptics/tipico) | ![Python package](https://github.com/ArcetriAdaptiveOptics/tipico/workflows/Python%20package/badge.svg) | [![codecov](https://codecov.io/gh/ArcetriAdaptiveOptics/tipico/branch/main/graph/badge.svg?token=ApWOrs49uw)](https://codecov.io/gh/ArcetriAdaptiveOptics/tipico) | [![Documentation Status](https://readthedocs.org/projects/tipico/badge/?version=latest)](https://tipico.readthedocs.io/en/latest/?badge=latest) | [![PyPI version](https://badge.fury.io/py/tipico.svg)](https://badge.fury.io/py/tipico)
[tipico_server](https://github.com/ArcetriAdaptiveOptics/tipico_server) | ![Python package](https://github.com/ArcetriAdaptiveOptics/tipico_server/workflows/Python%20package/badge.svg) | [![codecov](https://codecov.io/gh/ArcetriAdaptiveOptics/tipico_server/branch/main/graph/badge.svg?token=ApWOrs49uw)](https://codecov.io/gh/ArcetriAdaptiveOptics/tipico_server) | [![Documentation Status](https://readthedocs.org/projects/tipico_server/badge/?version=latest)](https://tipico_server.readthedocs.io/en/latest/?badge=latest) | [![PyPI version](https://badge.fury.io/py/tipico-server.svg)](https://badge.fury.io/py/tipico_server)



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

