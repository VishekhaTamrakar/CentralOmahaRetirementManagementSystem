import unittest
from unit_tests import mypkg
from unit_tests import resident, maintenanceworker

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.loader.findTestCases(resident))
test_suite.addTest(unittest.loader.findTestCases(maintenanceworker))

# Add your individual testcases here


# Wrapping up

unittest.TextTestRunner(verbosity=2).run(test_suite)
driver = mypkg.getOrCreateWebdriver()
driver.close()