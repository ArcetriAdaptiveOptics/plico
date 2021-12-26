#!/usr/bin/env python
import unittest
import os
from plico.utils.starter_script_creator_base import StarterScriptCreatorBase
import pathlib


class MyStarterScriptCreator(StarterScriptCreatorBase):

    def __init__(self):
        StarterScriptCreatorBase.__init__(self)
        self.destination_path = os.path.join('destination', 'path')
        self.executable = os.path.join('executable', 'module.py')
        self.config_section = 'my_config_section'

    def installExecutables(self):
        self._createAStarterScript(
            self.destination_path,
            self.executable,
            self.config_section
        )


class StarterScriptCreatorBaseTest(unittest.TestCase):

    TEST_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            "./tmp/")
    LOG_DIR = os.path.join(TEST_DIR, "log")
    CONF_FILE = os.path.join("path", "to", "config", "file.conf")
    BIN_DIR = os.path.join(TEST_DIR, "apps", "bin")
    SOURCE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                              "../..")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_script(self):
        ssc = MyStarterScriptCreator()
        ssc.setInstallationBinDir(self.BIN_DIR)
        ssc.setPythonPath(self.SOURCE_DIR)
        ssc.setConfigFileDestination(self.CONF_FILE)
        ssc.installExecutables()

        want_file_in = ssc.destination_path
        self.assertTrue(pathlib.Path(want_file_in).resolve().is_file())


if __name__ == "__main__":
    unittest.main()
