import webbrowser
from random import randint
import subprocess


class Commands():
    """
    Данный класс отвечает за выполнение команд.
    КАждый его метод выполняет определённую команду
    """
    def lms(self):
        webbrowser.open('https://smartedu.hse.ru/')

    def stop(self, text):
        if text == 'стоп':
            print('стоп')
    def calc(self):
        # subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        subprocess.Popen('calc.exe')

    def workout(self, exercise):
        task = exercise[randint(0, len(exercise) - 1)]
        value = randint(1, 20)

        print(task, value)

    def smart_find_app(name):
        subprocess.Popen(name)

    def smart_find_site(name):
        webbrowser.open(f'https://{name}')
    
    def hello(name):
        print(f'Привет {name}')

    def youtube(self):
        webbrowser.open('https://youtube.com/')
    def mail(self):
        webbrowser.open('https://mail.yandex.ru/')
    
