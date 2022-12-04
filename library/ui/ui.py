import os  # Импортируем библиотку для работы с ОС


def draw_ui(strings_ui: str):
    print(strings_ui)


def clear():
    clear_console = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear_console()


def print_books(books):
    book_list = ''
    index = 1

    for book in books:
        book_list += f'{index} - {book}\n'
        index += 1

    print(book_list)


def get_input():
    while True:
        user_input = input('Введите команду.\n')
        return user_input


def get_single_input():
    return input('Введите значение:\n')

def get_parameterized_input(text: str):
    return input(text + '\n')


def confirm_input():
    input("Нажмите Enter, чтобы продолжить...")


def get_sting():
    user_input = None
    while True:
        try:
            user_input = str(input('Введите строку число.\n'))
            return user_input
        except Exception as e:
            print(e)
