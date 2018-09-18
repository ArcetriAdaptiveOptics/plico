#!/usr/bin/env python
from setuptools import setup, Command




class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')
        
        sys.exit()

setup(name='plico',
      description='Python Laboratory Instrumentation COntrol',
      version='0.14',
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
