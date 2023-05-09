import unittest
from voice_helper import dispatcher
from main import Commands
import speech_recognition
from voice_helper import file_for_test

class MyTestCase(unittest.TestCase):
    '''
    By Artem
    Класс тестов
    '''

    def test_LMS(self):
        file__test_lms = file_for_test("files_for_tests/test_calc.wav")
        self.assertEqual(dispatcher(file__test_lms), True)

    def test_workout(self):
        file__test_workout = file_for_test("files_for_tests/check_workout.wav")
        self.assertEqual(dispatcher(file__test_workout), True)

    def test_show_time(self):
        file__test_date_and_time = file_for_test("files_for_tests/test_time.wav")
        self.assertEqual(dispatcher(file__test_date_and_time), True)

    def test_date(self):
        file__test_date_and_time = file_for_test("files_for_tests/test_date.wav")
        self.assertEqual(dispatcher(file__test_date_and_time), True)

    def test_hello(self):
        file__test_hello = file_for_test("files_for_tests/test_hello.wav")
        self.assertEqual(dispatcher(file__test_hello), True)

    def test_youtube(self):
        file__test_youtube = file_for_test("files_for_tests/test_youtube.wav")
        self.assertEqual(dispatcher(file__test_youtube), True)

    def test_death_note(self):
        file__test_death_note = file_for_test("files_for_tests/test_death_note.wav")
        self.assertEqual(dispatcher(file__test_death_note), True)

    def test_github(self):
        file__test_github = file_for_test("files_for_tests/test_github.wav")
        self.assertEqual(dispatcher(file__test_github), True)

    def test_calc(self):
        file_test_calc = file_for_test("files_for_tests/calc_test.wav")
        self.assertEqual(dispatcher(file_test_calc), True)


if __name__ == "__main__":
    unittest.main()
