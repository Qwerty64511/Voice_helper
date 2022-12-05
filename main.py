import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
def greeting():
    return "Охаё, Тёма кун"
def create_task():
    print("Что добавить в список дел?")
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language='eng-ENG').lower()

    with open('todo-list.txt','a',encoding='utf-8') as todo_list:
        todo_list.write(f'{query}\n')
    return f'Задача {query} добавлена в todo-list!'

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic,duration=0.5)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio,language='ru-RU').lower()

if query == "привет саша":
    print(greeting())
elif query == 'добавить задачу':
    print(create_task())
