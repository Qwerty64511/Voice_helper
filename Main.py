import webbrowser
from random import randint
import subprocess
import pyttsx3
import datetime
import pyaudio
import wave
import pymysql
import sqlite3 as sq

engine = pyttsx3.init()


def voice(text):
    engine.say(text)
    engine.runAndWait()


class Commands():
    """
    Данный класс отвечает за выполнение команд.
    КАждый его метод выполняет определённую команду
    """

    def lms(self):
        '''
        by Matvey
        Данная функция открывает Smart LMS
        :return: None
        '''
        webbrowser.open('https://smartedu.hse.ru/')
        voice('учитесь на здоровье')

    def calc(self):
        '''
        by Matvey
        Данная функция открывает калькулятор
        :return: None
        '''
        subprocess.Popen('calc.exe')

    def workout(self, exercise):
        """
        By Matvey
        Данная функция выдает случайное упраженение из списка и количество повторений, которое нужно выполнить
        :param exercise: список упражнений
        :return: None
        """
        task = exercise[randint(0, len(exercise) - 1)]
        value = randint(1, 20)

        voice(task + str(value))

    def smart_find_app(name):
        """
        By Michail
        Функция, осуществляющая поиск и открытие приложений по названию
        :return: None
        """
        subprocess.call(name)

    def smart_find_site(name):
        '''
        By Michail
        Функция, осуществляющая поиск и открытие сайтов по их адресу
        :return: None
        '''
        webbrowser.open(f'https://{name}')

    def hello(name):
        '''
        By Michail
        Функция, осуществляющее приветствие
        :return: None
        '''
        voice(f'Привет {name}')

    def youtube(self):
        '''
        By Michail
        Функция, открывающая Youtube
        :return: None
        '''
        webbrowser.open('https://youtube.com/')

    def mail(self):
        '''
        By Michail
        Функция, открывающая Mail
        :return: None
        '''
        webbrowser.open('https://mail.yandex.ru/')

    def github(self):
        '''
        By Michail
        Фунция, открывающая гитхаб
        :return: None
        '''
        webbrowser.open('https://github.com/')

    def Death_Note(self):
        '''
        By Artem
        Функция, открывающая сайт для просмотра аниме Death Note
        :return: None
        '''
        webbrowser.open('https://m.wcostream.net/anime/death-note')

    def date_and_time(self):
        '''
        By Artem
        Функция, показывающая текущую дату и текущее время
        :return: None
        '''
        try:
            date_object = str(datetime.datetime.now())
            lst = date_object.split(" ")
            date = lst[0].split("-")
            time = lst[1].split(":")
            voice("сегодня", str(date[2]), str(date[1]), str(date[0]), "время", str(time[0]), str(time[1]))
            return True
        except:
            return False

    def record_and_save_audio_file(self, number_of_records,RECORD_SECONDS,CHUNK=1024, FORMAT=pyaudio.paInt16, CHANNELS=2, RATE=44100):
        '''
        By Artem
        Функция осуществляющая запись и сохранение аудиофайлов
        :param number_of_records: количество записей
        :param CHUNK:
        :param FORMAT: формат
        :param CHANNELS: каналы
        :param RATE: частота
        :param RECORD_SECONDS: время записи
        :return: None
        '''
        for k in range(number_of_records):
            print("Введите название файла")
            WAVE_OUTPUT_FILENAME = input()
            WAVE_OUTPUT_FILENAME += ".wav"
            p = pyaudio.PyAudio()
            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            input_device_index=1,
                            frames_per_buffer=CHUNK)

            print("recording")
            frames = []
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)
            print("done recording")
            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
    def create_recipe_book(self):
        '''
        by Artem
        Создает книгу(таблицу) рецептов в базе данных recipes
        :return: None
        '''
        with sq.connect("recipes.db") as connection:
            Cursor = connection.cursor()

            Cursor.execute("""CREATE TABLE IF NOT EXISTS recipes (
            meal TEXT,
            recipe TEXT,
            cooking time INTEGER
            )""")
    def delete_recipe(self):
        '''
        By Artem
        Данная функция удаляет рецепт из книги(таблицы) рецептов
        :return: None
        '''
        meals = []
        try:
            with sq.connect("recipes.db") as connection:
                Cursor = connection.cursor()
                voice("Какой рецепт хотите удалить?")
                recipe_for_delete = input()
                Cursor.execute(f"""DELETE FROM recipes WHERE name == {recipe_for_delete}""")
                voice("Рецепт успешно удален")

        except:
            voice("Произошла какая-то ошибка")

    def add_recipes(self):
        '''
        By Artem
        Данная функция добавляет рецепт(ы) в книгу(таблицу) рецептов
        :return: None
        '''
        try:
            Recipes = []
            with sq.connect("recipes.db") as connection:
                Cursor = connection.cursor()
                voice("Сколько рецептов хотите внести?")
                n = int(input())
                for i in range(n):
                    voice("Введите название блюда")
                    Meal = input()
                    voice("Введите рецепт")
                    Recipe = input()
                    voice("Введите время приготовления")
                    Cooking_time = input()
                    tup = (Meal, Recipe, Cooking_time)
                    Recipes.append(tup)
                Cursor.executemany("INSERT INTO recipes VALUES(?, ?, ?)", Recipes)
                if len(Recipes) == 1:
                    voice("Рецепт успешно добавлен")
                else:
                    voice("Рецепты успешно добавлены")
        except:
            voice("Произошла какая-то ошибка")

    def print_recipes(self):
        '''
        By Artem
        Данная функция выводит рецепт определённого блюда
        :return: None
        '''
        meals = []
        try:
            with sq.connect("recipes.db") as connection:
                Cursor = connection.cursor()
                voice("Рецепт какого блюда хотите увидеть?")
                rec = input()
                Cursor.execute(f"SELECT meal,recipe,cooking time FROM recipes WHERE name = {rec}")


        except:
            voice("Такого блюда нет")