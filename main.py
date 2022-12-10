import webbrowser
from random import randint

import pyttsx3

engine = pyttsx3.init()


def voice(text):
    engine.say(text)
    engine.runAndWait()


class Commands():

    def lms(self):
        webbrowser.open('https://smartedu.hse.ru/')
        voice('учитесь на здоровье')

    def stop(self, text):
        if text == 'стоп':
            print('стоп')

    def workout(self, exercise):
        task = exercise[randint(0, len(exercise) - 1)]
        value = randint(1, 20)

        voice(task + str(value))
