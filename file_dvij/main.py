
#підключае файл з функціями для роботи з файлом
from os_com import *
#підключае файл з функціями для роботи з виглядом та функціоналом консолі 
from config import *


#Підказки 
def hints():
    print("\nКоманди:")
    print("Список файлів і папок - ls")
    print("Створити папку - mkdir")
    print("Видалити папку - rmdir")
    print("Перейменувати файл - mv")
    print("Видалити файл - rm")
    print("Перейти в вказану директорію - cd")
    print("Вивести вміст текстового файлу - cat")
    print("Зміна параметрів - config")
    print("Вийти - end \n\n\n")


#
def processing1(command, value1, value2):
    global show_hints
    global del_session
    if command == 'ls':  # ls для відображення списку файлів і папок
        list_files()

    elif command == 'mkdir':  # mkdir для створення папки
        create_directory(value1)

    elif command == 'rmdir':  # rmdir для видалення папки 
        delete_directory(value1)

    elif command == 'mv':  # mv перейменування
        rename_file(value1, value2)

    elif command == 'rm':  # rm для видалення файлу
        delete_file(value1)

    elif command == 'cd':  # cd для зміни робочої директорії
        change_directory(value1)

    elif command == 'cat':  # cat для відкриття текстових файлів
        open_file(value1)


    elif command == 'touch':#touch для створення файлу
        touch(value1)
    



    elif command == "config" or command == "conf":  # config для зміни вигляду
        show_config()
        name_conf = input("\033[31mВведіть назву налаштування: \033[0m")

        if name_conf == "show_hints":  # Підказки
            new_value = input("Введіть нове значення show_hints (True/False): ")
            change_show_hints(new_value)
            if new_value.lower() == 'true':
                show_hints = True
            elif new_value.lower() == 'false':
                show_hints = False

        elif name_conf == "del_session":  # del_session
            new_value = input("Введіть нове значення del_session (True/False): ")
            change_del_session(new_value)
            if new_value.lower() == 'true':
                del_session = True
            elif new_value.lower() == 'false':
                del_session = False

        else:
            print(f"\033[94mПараметр {name_conf} не знайдено. \033[0m")

    else:
        print("Некоректний ввід. Спробуйте знову.")





#костиль для корекного відтворення кольорів 
print("\033[94m\033[0m")
os.system('cls' if os.name == 'nt' else 'clear')

#Цикл для постійної роботи консолі 
while True:


    if show_hints:
        hints()

    choice = input(f"\033[94m{os.getcwd()} >>> \033[0m")

    
    if len(choice.split()) >= 4 :
        ptint("Некоректний ввід. Спробуйте знову.")
    else :
        command = choice.split()[0] if choice else None
        value1 = choice.split()[1] if len(choice.split()) > 1 else None
        value2 = choice.split()[2] if len(choice.split()) > 2 else None
        if command and command != 'end': 
            processing1(command, value1, value2)
        elif command == 'end':  # end завершення сеансу
            break
        else:
            print("Некоректний ввід. Спробуйте знову.")

    


    
    #Обновлює консоль
    if del_session:
        input("Нтисніть Enter для продовження...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана терминала
