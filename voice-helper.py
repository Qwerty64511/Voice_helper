import speech_recognition

exercise = ['Отжимания', 'подтягивания']

def dispatcher(record):
    if record == 'открой дневник':
        Commands.lms(self=record)

    if record == 'выдай упражнения':
        Commands.workout(self=record, exercise=exercise)

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
            print('check your microphone')

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
        print('тут будет открытие лмс...')

    def stop(self, text):
        if text == 'стоп':
            print('стоп')

    def workout(self, exercise):
        print('тут будет i.rand(exercise)')

if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    while True:
        # старт записи речи с последующим выводом распознанной речи
        voice_input = record_and_recognize_audio()
        print(voice_input, '-- финальная расшифровка')

        dispatcher(voice_input)
