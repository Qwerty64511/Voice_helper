import speech_recognition
import webbrowser
import random
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def Sonechka_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
    except speech_recognition.UnknownValueError:
        return "Не понял..."


def random_exercize():
    List_of_exercises = ["Отжимания", "Подтягивания","Приседания","Пресс","Бег"]
    request = Sonechka_command()
    if request == "случайное упражнение":
        exercise = random.randint(0,len(List_of_exercises))[List_of_exercises]
        return exercise

def Open():
    request = Sonechka_command()
    if request == "открой смартлмс":
        webbrowser.open('https://smartedu.hse.ru/courses', new=2)
    elif request == "открой лмс":
        webbrowser.open('https://lms.hse.ru/',new=2)
    elif request == "открой вк":
        webbrowser.open('https://vk.com', new=2)
    elif request == "открой тетрадь смерти":
        webbrowser.open('https://m.wcostream.net/anime/death-note',new=2)



def main():
    request = Sonechka_command()
    if request == "привет соня":
        print(greeting())
    elif request == 'добавить задачу':
        print(task_list())
    elif request == "открой смартлмс":
        webbrowser.open('https://smartedu.hse.ru/courses', new=2)
    elif request == 'случайное упражнение':
        print(random_exercize())

def greeting():
    return "Охаё, Тёма кун"

def task_list():
    print("Что добавить в список дел?")
    task = Sonechka_command()
    with open('todo-list.txt', 'a', encoding='utf-8') as todo_list:
        todo_list.write(f'{task}\n')
    return f'Задача {task} добавлена в todo-list!'

if __name__ == "__main__":
    main()
# git push -f - НЕ ДЕЛАТЬ!!!!!!!!!