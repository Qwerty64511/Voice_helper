import unittest
from voice_helper import dispatcher
from main import Commands
import speech_recognition
from voice_helper import file_for_test
from voice_helper import exercises
class MyTestCase(unittest.TestCase):
    def test_LMS(self):
        file__check_lms = file_for_test("check_lms.wav")
        self.assertEqual(dispatcher(file__check_lms),Commands.lms(self=file__check_lms) )

    def test_workout(self):
        file_test_workout = file_for_test("check_workout.wav")
        self.assertEqual(dispatcher(file_test_workout),Commands.workout(self=file_test_workout,exercise=exercises))

    def test_date_and_time(self):
        file_test_date_and_time = file_for_test("check_date_and_time.wav")
        self.assertEqual(dispatcher(file_test_date_and_time),Commands.date_and_time(self=file_test_date_and_time))


if __name__ == "__main__":
    unittest.main()