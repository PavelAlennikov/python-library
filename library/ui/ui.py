import os  # Импортируем библиотку для работы с ОС


def draw_ui(strings_ui: str):
    print(strings_ui)


def clear():
    clear_console = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear_console()


def get_input():
    while True:
        user_input = input('Введите команду.\n')
        return user_input


def get_single_input():
    return input('Введите значение:\n')


def get_sting():
    user_input = None
    while True:
        try:
            user_input = str(input('Введите строку число.\n'))
            return user_input
        except Exception as e:
            print(e)
