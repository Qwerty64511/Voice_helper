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
        webbrowser.open('https://smartedu.hse.ru/')
        voice('учитесь на здоровье')

    def stop(self, text):
        if text == 'стоп':
            print('стоп')
            
    def calc():
        subprocess.Popen('calc.exe')

    def workout(self, exercise):
        task = exercise[randint(0, len(exercise) - 1)]
        value = randint(1, 20)

        voice(task + str(value))

    def smart_find_app(name):
        subprocess.call(name)

    def smart_find_site(name):
        webbrowser.open(f'https://{name}')
    
    def hello(name):
        voice(f'Привет {name}')

    def youtube():
        webbrowser.open('https://youtube.com/')

    def mail():
        webbrowser.open('https://mail.yandex.ru/')

    def github():
        webbrowser.open('https://github.com/')

    def Death_Note(self):
        webbrowser.open('https://m.wcostream.net/anime/death-note')

    def date_and_time(self):
        try:
            date_object = str(datetime.datetime.now())
            lst = date_object.split(" ")
            date = lst[0].split("-")
            time = lst[1].split(":")
            print("сегодня", date[2], date[1], date[0], "время", time[0], time[1])
            return True
        except:
            return False

    def record_and_save_audio_file(self,number_of_records, CHUNK=1024, FORMAT=pyaudio.paInt16, CHANNELS=2, RATE=44100,
                                   RECORD_SECONDS=5):

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

    def connection_with_data_base(self):
        Recipes = []
        with sq.connect("recipes.db") as connection:
            Cursor = connection.cursor()

            Cursor.execute("""CREATE TABLE IF NOT EXISTS recipes (
                meal TEXT,
                recipe TEXT,
                cooking time INTEGER
                
                
            )""")
            print("Сколько рецептов хотите внести?")
            n = int(input())
            for i in range(n):
                print("Введите название блюда")
                Meal = input()
                print("Введите рецепт")
                Recipe = input()
                print("Введите время приготовления")
                Cooking_time = input()
                tup = (Meal,Recipe,Cooking_time)
                Recipes.append(tup)
            Cursor.executemany("INSERT INTO recipes VALUES(?, ?, ?)",Recipes)


            #Cursor.execute("""DELETE FROM recipes WHERE rowid == 1""")

        print("Соединение успешно")
    
    
