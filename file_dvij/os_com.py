# Імпортуємо бібліотеку для роботи з ОС
import os
# Додатковий файл для роботи з файлами і директоріями
import shutil


# Повертає список ЛОКАЛЬНИХ файлів
def list_files():
    files = os.listdir('.')
    for file in files:
        print(f"\033[32m{file}\033[0m")

# Створюємо папку
def create_directory(directory_name):
    if directory_name == None:
        directory_name = input("\033[94mВведіть ім'я папки: \033[0m")
    os.mkdir(directory_name)
    print(f"Створена папка '{directory_name}'")

# Перейменовуємо файл
def rename_file(old_name, new_name):
    if new_name == None:
        old_name = input("\033[94mВведіть поточне ім'я файлу: \033[0m")
        new_name = input("\033[94mВведіть нове ім'я файлу: \033[0m")
    try:
        os.rename(old_name, new_name)
        print(f"Файл '{old_name}' перейменовано в '{new_name}'")
    except FileNotFoundError:
        print(f'Файл {old_name} не знайдено.')

# !!! ДЛЯ ВИДАЛЕННЯ ПАПКИ І ФАЙЛІВ ВИКОРИСТОВУЮТЬСЯ РІЗНІ КОМАНДИ !!!
# Видаляємо папку (регістрозалежно)
def delete_directory(directory_name):
    if directory_name == None:
        directory_name = input("\033[94mВведіть ім'я папки: \033[0m ")
    shutil.rmtree(directory_name)
    print(f"Видалена папка '{directory_name}'")

# Видаляємо файл (регістрозалежно)
def delete_file(file_name):
    if file_name == None:
        file_name = input("\033[94mВведіть ім'я файлу: \033[0m")
    try:
        os.remove(file_name)
        print(f"Видалений файл '{file_name}'")
    except FileNotFoundError:
        print(f'Файл {file_name} не знайдено.')

# Для переміщення між папками
def change_directory(directory_path):
    if directory_path == None:
        directory_path = input('\033[94mВведіть ім\'я/шлях папки: \033[0m')
    try:
        os.chdir(directory_path)
    except FileNotFoundError:
        print(f'Директорія {directory_path} не знайдено.')

# Відкриваємо файл
def open_file(file_name):
    if file_name == None:
        file_name = input("\033[94mВведіть ім'я файлу:\033[0m ")
    print("\n\n\n")
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except IsADirectoryError:
        print(f"'{file_name}' є папкою.")
    except PermissionError:
        print(f"Немає доступу до файлу '{file_name}'.")
    except Exception as e:
        print(f"Сталася помилка: {e}")


#створення файлу 
def touch(path):
    if path == None :
        path = input("\033[94mВведіть ім'я для файлу:\033[0m ")
    try:
        with open(path, 'a'):
            os.utime(path, None)
    except OSError as e:
        print(f"Сталася помилка при створенні файлу: {e}")



    
