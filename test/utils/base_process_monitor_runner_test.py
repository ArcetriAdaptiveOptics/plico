import os
import sys
import subprocess
import shutil
import unittest
import logging
import numpy as np
from test.test_helper import TestHelper, Poller, MessageInFileProbe, \
    ExecutionProbe
from plico.utils.base_process_monitor_runner import BaseProcessMonitorRunner

from plico.utils.logger import Logger
from plico.utils.configuration import Configuration
from plico_motor_server.utils.starter_script_creator import \
    StarterScriptCreator
from plico_motor_server.utils.process_startup_helper import \
    ProcessStartUpHelper

from functools import wraps

CONF_STRING = '''
[test_server1]
foo = 'bar1'

[test_server2]
foo = 'bar2'

[processMonitor]
spawn_delay = 2

[global]
app_name= inaf.arcetri.ao.plico
app_author= INAF Arcetri Adaptive Optics
python_package_name=plico
'''

class TestRunner(BaseProcessMonitorRunner):
    def __init__(self):
        super.__init__(name='TestRunner',
                       server_config_prefix='test_server',
                       runner_config_section='runner',
                       server_process_name='test_server',
                       process_monitor_port=8000)


def _dumpEnterAndExit(enterMessage, exitMessage, f, self, *args, **kwds):
    doDump = True
    if doDump:
        print(enterMessage)
    res = f(self, *args, **kwds)
    if doDump:
        print(exitMessage)
    return res


def dumpEnterAndExit(enterMessage, exitMessage):

    def wrapperFunc(f):

        @wraps(f)
        def wrapper(self, *args, **kwds):
            return _dumpEnterAndExit(enterMessage, exitMessage,
                                     f, self, *args, **kwds)

        return wrapper

    return wrapperFunc


@unittest.skipIf(sys.platform == "win32",
                 "Integration test doesn't run on Windows. Fix it!")
class IntegrationTest(unittest.TestCase):

    TEST_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            "./tmp/")
    LOG_DIR = os.path.join(TEST_DIR, "log")
    CALIB_FOLDER = 'test/integration/calib'
    CONF_SECTION = 'processMonitor'
    SERVER_LOG_PATH = os.path.join(LOG_DIR, "%s.log" % CONF_SECTION)
    SERVER_PREFIX = 'test_server'
    BIN_DIR = os.path.join(TEST_DIR, "apps", "bin")
    CONF_DIR = os.path.join(TEST_DIR, "conf")
    CONF_FILE = os.path.join(CONF_DIR, 'plico_test_runner.conf')

    SOURCE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                              "../..")

    def setUp(self):
        self._setUpBasicLogging()
        self.server = None
        self._wasSuccessful = False

        self._removeTestFolderIfItExists()
        self._makeTestDir()
        self._writeConfFile()
        self.configuration = Configuration()
        self.configuration.load(self.CONF_FILE)

        calibrationRootDir = self.configuration.calibrationRootDir()
        self._setUpCalibrationTempFolder(calibrationRootDir)
        print("Setup completed")

    def _setUpBasicLogging(self):
        logging.basicConfig(level=logging.DEBUG)
        self._logger = Logger.of('Integration Test')

    def _makeTestDir(self):
        os.makedirs(self.TEST_DIR)
        os.makedirs(self.LOG_DIR)
        os.makedirs(self.BIN_DIR)
        os.makedirs(self.CONF_DIR)

    def _writeConfFile(self):
        with open(self.CONF_FILE, 'w') as f:
            f.write(CONF_STRING)

    def _setUpCalibrationTempFolder(self, calibTempFolder):
        shutil.copytree(self.CALIB_FOLDER,
                        calibTempFolder)

    def _removeTestFolderIfItExists(self):
        if os.path.exists(self.TEST_DIR):
            shutil.rmtree(self.TEST_DIR)

    @dumpEnterAndExit("tearing down", "teared down")
    def tearDown(self):
        TestHelper.dumpFileToStdout(self.SERVER_LOG_PATH)

        if self.server is not None:
            TestHelper.terminateSubprocess(self.server)

        if self._wasSuccessful:
            self._removeTestFolderIfItExists()

    @dumpEnterAndExit("creating starter scripts", "starter scripts created")
    def _createStarterScripts(self):
        ssc = StarterScriptCreator()
        ssc.setInstallationBinDir(self.BIN_DIR)
        ssc.setPythonPath(self.SOURCE_DIR)
        ssc.setConfigFileDestination('$1') # Allow config file to be a script parameter
        ssc.installExecutables()

    @dumpEnterAndExit("starting processes", "processes started")
    def _startProcesses(self):
        psh = ProcessStartUpHelper()
        serverLog = open(os.path.join(self.LOG_DIR, "server.out"), "wb")
        self.server = subprocess.Popen(
            [psh.processProcessMonitorStartUpScriptPath(),
             self.CONF_FILE,
             self.CONF_SECTION],
            stdout=serverLog, stderr=serverLog)
        Poller(5).check(MessageInFileProbe(
            TestRunner.RUNNING_MESSAGE, self.SERVER_LOG_PATH))

    def _testProcessesActuallyStarted(self):
        controllerLogFile = os.path.join(
            self.LOG_DIR,
            '%s%d.log' % (SERVER_PREFIX, 1))
        Poller(5).check(MessageInFileProbe(
            TestRunner.RUNNING_MESSAGE, controllerLogFile))
        controller2LogFile = os.path.join(
            self.LOG_DIR,
            '%s%d.log' % (SERVER_PREFIX, 2))
        Poller(5).check(MessageInFileProbe(
            TestRunner.RUNNING_MESSAGE, controller2LogFile))

    def test_main(self):
        self._buildClients()
        self._createStarterScripts()
        self._startProcesses()
        self._testProcessesActuallyStarted()
        self._wasSuccessful = True


if __name__ == "__main__":
    unittest.main()

