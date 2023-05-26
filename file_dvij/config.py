# Імпортуємо бібліотеку для роботи з конфігураційними файлами
import configparser
# Імпортуємо бібліотеку для роботи з ОС
import os

#для роботи с одной  переменой


config_file = 'config.ini'
config_parser = configparser.ConfigParser()

# Загрузка значения из INI-файла
config_parser.read(config_file)

show_hints = config_parser.getboolean('Settings', 'show_hints')


#отображает все параметри 
def show_config():
    for section in config_parser.sections():
        print(f"[{section}]")
        for key, value in config_parser.items(section):
            print(f"{key} = {value}")


#отображение подсказок 
def change_show_hints(new_value):
    if new_value.lower() == 'true':
        show_hints = True  # Обновление переменной show_hints внутри функции
        config_parser.set('Settings', 'show_hints', 'True')  # Обновление значения в INI-файле
        with open(config_file, 'w') as file:
            config_parser.write(file)
        print("Значение show_hints успешно изменено.")
    elif new_value.lower() == 'false':
        show_hints = False  # Обновление переменной show_hints внутри функции
        config_parser.set('Settings', 'show_hints', 'False')  # Обновление значения в INI-файле
        with open(config_file, 'w') as file:
            config_parser.write(file)
        print("Значение show_hints успешно изменено.")
    else: 
        print(f"Неверное значение  ")




# Сохранение значения в INI-файле
with open(config_file, 'w') as file:
    config_parser.write(file)