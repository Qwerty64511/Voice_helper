import unittest
from Voice_helper import dispatcher
from Main import Commands
class MyTestCase(unittest.TestCase):
    def LMS_test_(self,test_lms):
        self.assertEqual(dispatcher(test_lms),Commands.lms())  # add assertion here



