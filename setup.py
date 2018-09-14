#!/usr/bin/env python
from setuptools import setup


__version__ = "$Id: setup.py 56 2018-09-14 16:42:15Z lbusoni $"



setup(name='plico',
      description='Python Laboratory Instrumentation COntrol',
      version='0.13',
      classifiers=['Development Status :: 4 - Beta',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   ],
      long_description=open('README.md').read(),
      url='',
      author_email='lbusoni@gmail.com',
      author='Lorenzo Busoni',
      license='',
      keywords='laboratory, instrumentation control',
      packages=['plico',
                'plico.client',
                'plico.rpc',
                'plico.types',
                'plico.utils',
                ],
      install_requires=["numpy",
                        "psutil",
                        "configparser",
                        "six",
                        "appdirs",
                        "pyzmq",
                        "futures",
                        "pyfits",
                        ],
      include_package_data=True,
      test_suite='test',
      )
