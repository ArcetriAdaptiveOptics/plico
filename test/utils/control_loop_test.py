import unittest
from plico.utils.control_loop import IntolerantControlLoop
from plico.utils.stepable import Stepable

class MyException(Exception):
    pass

class RaisingStepable(Stepable):
        
    def step(self):
        raise MyException()
    
    def isTerminated(self):
        return False

class ControlLoopTest(unittest.TestCase):

    def test_untolerant_loop_always_raises(self):
        raising_stepable = RaisingStepable()
        logger = None
        loop = IntolerantControlLoop(raising_stepable, logger)
        self.assertRaises(MyException, loop.start)


if __name__ == "__main__":
    unittest.main()
