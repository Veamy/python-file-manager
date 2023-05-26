
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


#Цикл для постійної роботи консолі 
while True:
    print(os.getcwd())  # Вивести поточний робочий каталог

    if show_hints:
        hints()

    choice = input("Введіть команду: ")

    if choice == 'ls':#ls для відображання списока файлів і папок
        list_files()

    elif choice == 'mkdir':#mkdir для створення папки
        directory_name = input("Введіть ім'я папки: ")
        create_directory(directory_name)

    elif choice == 'rmdir':#rmdir для видалення папки
        directory_name = input("Введіть ім'я папки: ")
        delete_directory(directory_name)

    elif choice == 'mv':#mv перейменування 
        old_name = input("Введіть поточне ім'я файлу: ")
        new_name = input("Введіть нове ім'я файлу: ")
        rename_file(old_name, new_name)

    elif choice == 'rm':#rm для виделення файлу
        file_name = input("Введіть ім'я файлу: ")
        delete_file(file_name)

    elif choice == 'cd':#cd для зміни робочої директоріі
        directory_path = input('Введіть ім\'я/шлях папки:')
        change_directory(directory_path)

    elif choice == 'cat':#cat для відкриття текстових файлів
        file_name = input("Введіть ім'я файлу: ")
        print("\n\n\n")
        open_file(file_name)

    elif choice == "config" or choice == "conf":#config для зміни вигляду
        show_config()
        name_conf = input("Введіть нову назву налаштування: ")

        if name_conf == "show_hints":#Підказки
            new_value = input("Введіть нове значення show_hints (True/False): ")
            change_show_hints(new_value)
            if new_value.lower() == 'true':
                show_hints = True
            elif new_value.lower() == 'false':
                show_hints = False

        else:
            print(f"Параметр {name_conf} не знайдено.")

    elif choice == 'end':#end завершення сеансу
        break
    else:
        print("Некоректний ввід. Спробуйте знову.")


    
    #Оновлює консоль
    input("Натисніть Enter для продовження...")
    os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана терминала
