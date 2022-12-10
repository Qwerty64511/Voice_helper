import webbrowser
from random import randint
import subprocess


class Commands():

    def lms(self):
        webbrowser.open('https://smartedu.hse.ru/')

    def stop(self, text):
        if text == 'стоп':
            print('стоп')
            
    def calc():
        subprocess.Popen('calc.exe')

    def workout(self, exercise):
        task = exercise[randint(0, len(exercise) - 1)]
        value = randint(1, 20)

        print(task, value)

    def smart_find_app(name):
        subprocess.call(name)

    def smart_find_site(name):
        webbrowser.open(f'https://{name}')
    
    def hello(name):
        print(f'Привет {name}')

    def youtube():
        webbrowser.open('https://youtube.com/')
    def mail():
        webbrowser.open('https://mail.yandex.ru/')
    def github():
        webbrowser.open('https://github.com/')
    
