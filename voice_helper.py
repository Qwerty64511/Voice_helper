import speech_recognition
from main import Commands, voice
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 200)

tools = {
}


def dispatcher(record):
    """
    данная функция отвечает за обработку поступивших команд
    :param record: record - расшифровка голосовой команды
    :return: данная функция ничего не возвращает. Она вызывает класс Commands в котором происходит выполнение команд
    """
    splited_record = record.split(' ')
    try:
        if record == 'открой lms' or record == 'открой лмс':
            Commands.lms(self=record)

        elif record == 'открой калькулятор':
            Commands.calc()

        elif record == 'открой ютуб' or record == 'открой youtube':
            Commands.youtube()
            
        elif record == 'открой гитхаб' or record == 'github':
            Commands.github()

        elif record == 'открой почту':
            Commands.mail()
        
        elif splited_record[0] == 'открой' and 'com' not in splited_record[1] and 'ru' not in splited_record[1]:
            Commands.smart_find_app(splited_record[1])

        elif splited_record[0] == 'открой':
            Commands.smart_find_site(splited_record[1])

        elif record == 'выдай упражнения':
            exercise = ['Отжимания', 'подтягивания']
            Commands.workout(self=record, exercise=exercise)

        elif record == 'меня зовут миша' or record =='меня зовут артём'or record =='меня зовут матвей':
            Commands.hello(name=record[11:])

        else:
            raise ValueError

    except ValueError:
        voice('нормально говори дебил')


def listner():
    """
    Данная функция записывает голосовую команду
    :return: данная функция возвращает аудиофайл
    """
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
    """
    данная функция распознаёт принимаемый аудиофайл и занимается переводом звука в текст
    :param audio: принимает аудиофайл
    :return: возвращает расшифровку команды
    """
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
    """
    Данная функция является основной в нашем проекте. Она отвечает за навигацию по всему проекту и первичную обработку
    поступивших команд
    :return: Она ничего не возвращает, лишь отвечает за навигацию
    """
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    tools['recognizer'] = recognizer
    tools['microphone'] = microphone

    audio = listner()
    voice_input = recognize(audio=audio).lower()

    if 'афанасий' in voice_input:
        voice_input = voice_input.replace('афанасий ', '')

        if len(voice_input) > 0:
            print('нашёл команды')
            dispatcher(voice_input)

    elif 'тесты' in voice_input:
        ...

    if 'стоп' in voice_input:
        return 0

    else:
        start()


#       тут будут тесты.
# if __name__ == "__main__":
#     while True:
start()
