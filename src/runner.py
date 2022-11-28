import sys
import unittest
from importlib import import_module
from src.io import *

is_testing = '-t' in sys.argv
day = sys.argv.pop()
file = import_module(f"src.d{day}")

if is_testing:
    class Test(unittest.TestCase):
        def runTest(self):
            file.test(read_example(day))
    suite = unittest.TestSuite()
    suite.addTest(Test())
    unittest.TextTestRunner().run(suite)
else:
    file.answer(read_input(day))