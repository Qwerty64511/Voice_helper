import speech_recognition
import webbrowser
from random import randint
def dispatcher(record):
    if record == 'открой дневник':
        Commands.lms(self=record)

    else:
        raise ValueError

def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознавание аудио
    """
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

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


class Commands():

    def lms(self):
        webbrowser.open('https://smartedu.hse.ru/')

    def stop(self, text):
        if text == 'стоп':
            print('стоп')

    def workout(self, exercise):
        task = exercise[randint(0, len(exercise)-1)]
        print(task)

if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    while True:
        # старт записи речи с последующим выводом распознанной речи
        voice_input = record_and_recognize_audio()
        print(voice_input)

# git push -f - НЕ ДЕЛАТЬ!!!!!!!!!