import unittest

test_lab_4_suite = unittest.TestSuite()

from test_task_4_1 import test_Task_1
test_lab_4_suite.addTest(unittest.makeSuite(test_Task_1))

from test_task_4_2 import test_Task_2
test_lab_4_suite.addTest(unittest.makeSuite(test_Task_2))

from test_task_4_3 import test_Task_3
test_lab_4_suite.addTest(unittest.makeSuite(test_Task_3))


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_lab_4_suite)
    print(f'Errors: {len(result.errors)}')
    print(f'Failures: {len(result.failures)}')
    print(f'Skipped: {len(result.skipped)}')