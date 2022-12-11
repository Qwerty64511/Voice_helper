import unittest
from Voice_helper import dispatcher
from Main import Commands
import speech_recognition
from Voice_helper import file_for_test
from Voice_helper import exercises
class MyTestCase(unittest.TestCase):
    def test_LMS(self):
        file__check_lms = file_for_test("check_lms.wav")
        self.assertEqual(dispatcher(file__check_lms),True)

    def test_workout(self):
        file_test_workout = file_for_test("check_workout.wav")
        self.assertEqual(dispatcher(file_test_workout),True)

    def test_date_and_time(self):
        file_test_date_and_time = file_for_test("check_date_and_time.wav")
        self.assertEqual(dispatcher(file_test_date_and_time),True)





if __name__ == "__main__":
    unittest.main()


