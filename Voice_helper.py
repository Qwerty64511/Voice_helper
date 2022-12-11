import speech_recognition
import webbrowser
from random import randint
import datetime
import pyaudio
import wave
from Main import Commands
import Voice_helper_tests
exercises = ['Отжимания','Подтягивания','Приседания','Бег','Пресс']

tools = {
}

def dispatcher(record):
    try:
        if record == 'открой дневник':
            Commands.lms(self=record)
        elif record == 'выдай упражнения':
            Commands.workout(self=record, exercise=exercises)
        elif record == 'который час':
            Commands.date_and_time(self=record)
        elif record == 'открой тетрадь смерти':
            Commands.Death_Note(self=record)
        elif record == 'хочу записать файл':
            print("Сколько файлов вы хотите записать?")
            count = int(input())  # количество файло
            Commands.record_and_save_audio_file(self=record, number_of_records=count)
        elif record == "открой рецепты":
            Commands.data_base(self=record)



        else:
            raise ValueError
        return True

    except ValueError:
        print('нормально говори дебил')
        return False


def listener():
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
def file_for_test(audio_file):
        r = speech_recognition.Recognizer()
        with speech_recognition.AudioFile(audio_file) as source:
            audio = r.listen(source)
            file = r.recognize_google(audio, language='RU').lower()
        return file
def start():
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    tools['recognizer'] = recognizer
    tools['microphone'] = microphone

    audio = listener()
    voice_input = recognize(audio=audio).lower()

    if 'афанасий' in voice_input:
        voice_input = voice_input.replace('афанасий ', '')

        if len(voice_input) > 0:
            dispatcher(voice_input)


if __name__ == "__main__":
    while True:
        start()