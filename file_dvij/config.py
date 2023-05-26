# Імпортуємо бібліотеку для роботи з конфігураційними файлами
import configparser
# Імпортуємо бібліотеку для роботи з операційною системою
import os

# Задаємо шлях до конфігураційного файлу
config_file = 'config.ini'
config_parser = configparser.ConfigParser()

# Завантажуємо значення з INI-файлу
config_parser.read(config_file)

show_hints = config_parser.getboolean('Settings', 'show_hints')


# Функція для відображення всіх параметрів конфігурації
def show_config():
    for section in config_parser.sections():
        print(f"[{section}]")
        for key, value in config_parser.items(section):
            print(f"{key} = {value}")


# Функція для зміни параметра show_hints
def change_show_hints(new_value):
    if new_value.lower() == 'true':
        show_hints = True  # Оновлюємо змінну show_hints всередині функції
        config_parser.set('Settings', 'show_hints', 'True')  # Оновлюємо значення в INI-файлі
        with open(config_file, 'w') as file:
            config_parser.write(file)
        print("Значення show_hints успішно змінено.")
    elif new_value.lower() == 'false':
        show_hints = False  # Оновлюємо змінну show_hints всередині функції
        config_parser.set('Settings', 'show_hints', 'False')  # Оновлюємо значення в INI-файлі
        with open(config_file, 'w') as file:
            config_parser.write(file)
        print("Значення show_hints успішно змінено.")
    else: 
        print("Невірне значення")


# Збереження значення в INI-файлі
with open(config_file, 'w') as file:
    config_parser.write(file)
