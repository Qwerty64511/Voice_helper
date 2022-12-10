import speech_recognition
from main import Commands
import subprocess

tools = {
}


def dispatcher(record):
    try:
        if record == 'открой lms':
            Commands.lms(self=record)

        elif record == 'открой калькулятор':
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')

        elif record == 'выдай упражнения':
            exercise = ['Отжимания', 'подтягивания']
            Commands.workout(self=record, exercise=exercise)

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
            print('Начинаю обработку')
            dispatcher(voice_input)

    if 'тесты' in voice_input:
        ...


#       тут будут тесты.
if __name__ == "__main__":
    while True:
        start()
