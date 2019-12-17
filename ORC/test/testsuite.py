import unittest
from unit_tests import mypkg
from unit_tests import test1

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.loader.findTestCases())
test_suite.addTest(unittest.loader.findTestCases())

# Add your individual testcases here


# Wrapping up

unittest.TextTestRunner(verbosity=2).run(test_suite)
driver = mypkg.getOrCreateWebdriver()
driver.close()