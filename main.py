import webbrowser
from random import randint


class Commands():

    def lms(self):
        webbrowser.open('https://smartedu.hse.ru/')

    def stop(self, text):
        if text == 'стоп':
            print('стоп')

    def workout(self, exercise):
        task = exercise[randint(0, len(exercise) - 1)]
        value = randint(1, 20)

        print(task, value)
    def smart_find(self, string):
        pass

    def hello(name):
        print(f'Привет {name}')
    def youtube():
        webbrowser.open('https://www.youtube.com/')
    
