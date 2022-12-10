import speech_recognition
import webbrowser
from random import randint
import datetime
import pyaudio
import wave
from Main import Commands
exercise = ['Отжимания','Подтягивания','Приседания','Бег','Пресс']

tools = {
}

def dispatcher(record):
    try:
        if record == 'открой дневник':
            Commands.lms(self=record)
        elif record == 'выдай упражнения':
            Commands.workout(self=record, exercise=exercise)
        elif record == 'который час':
            Commands.data_and_time(self=record)
        elif record == 'открой тетрадь смерти':
            Commands.Death_Note(self=record)
        elif record == 'хочу записать файл':
            print("Сколько файлов вы хотите записать?")
            count = int(input())  # количество файло
            Commands.record_and_save_audio_file(self=record, number_of_records=count)

        else:
            raise ValueError

    except ValueError:
        print('нормально говори дебил')


def listner():
    microphone = tools['microphone']
    recognizer = tools['recognizer']

    with microphone:

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)
            return audio

        except speech_recognition.WaitTimeoutError:
            print('check your microphone')


def recognize(audio):
    recognizer = tools['recognizer']

    recognized_data = ""
    # использование online-распознавания через Google

    try:
        print("Started recognition...")
        recognized_data = recognizer.recognize_google(audio, language="ru").lower()

    except speech_recognition.UnknownValueError:
        pass

    # в случае проблем с доступом в Интернет происходит выброс ошибки
    except speech_recognition.RequestError:
        print("Check your Internet Connection, please")

    return recognized_data


def start():
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    tools['recognizer'] = recognizer
    tools['microphone'] = microphone

    audio = listner()
    voice_input = recognize(audio=audio).lower()

    if 'афанасий' in voice_input:
        voice_input = voice_input.replace('афанасий ', '')

        if len(voice_input) > 0:
            dispatcher(voice_input)

    if 'тесты' in voice_input:
        ...


#       тут будут тесты.


def working():
    if __name__ == "__main__":

        # инициализация инструментов распознавания и ввода речи
        while True:
            # старт записи речи с последующим выводом распознанной речи
            audio = listner()
            voice_input = recognize(audio=audio)

            print(voice_input, '-- финальная расшифровка')

            try:
                dispatcher(voice_input)

            except ValueError:
                print('Я не нашёл команду')


if __name__ == "__main__":
    while True:
        start()