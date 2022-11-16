from model.book import Book
from repository.library import BookRep
from ui import ui as ui
from model.command import Command
from model.actions import Actions
from model.event import Event


class State:
    def __init__(self, header: str, command_list):
        self.__header = header
        self.__command_list = command_list

    def __str__(self):
        string_command_list = ''

        for command in self.__command_list:
            string_command_list += command.to_string() + '\n'

        return f'{self.__header}\n{string_command_list}'

    def to_string(self, state_manager):
        string_command_list = ''

        for command in self.__command_list:
            string_command_list += command.to_string() + '\n'

        return f'{self.__header}\n{string_command_list}'

    def handle_input(self, state_manager):
        pass


class StateWithStats(State):
    def to_string(self, state_manager):
        return super().to_string(state_manager) % state_manager.book_rep.count()


class MainState(StateWithStats):
    def handle_input(self, state_manager):
        user_input = ui.get_input()
        if user_input == Actions.Exit.value:
            state_manager.change_state(States.Exit)
        elif user_input == Actions.AddBook.value:
            state_manager.change_state(States.AddBook)
        elif user_input == Actions.RemoveBook.value:
            state_manager.change_state(States.RemoveBook)
        elif user_input == Actions.FindBook.value:
            print('FindBook')
        elif user_input == Actions.PrintAt.value:
            print('PrintAt')
        elif user_input == Actions.PrintAll.value:
            state_manager.change_state(States.PrintAll)
        else:
            pass  # TODO incorrect input


class PrintAllState(StateWithStats):
    def handle_input(self, state_manager):
        book_list = ''
        library = state_manager.book_rep.get_all()
        index = 1
        for book in library:
            book_list += f'{index} - {book}\n'
            index += 1
        ui.draw_ui(book_list)
        ui.get_sting()
        ui.clear()
        state_manager.change_state(States.Main)


class ExitState(State):
    def handle_input(self, state_manager):
        state_manager.stop_work()


class AddBookState(State):
    def __init__(self, header: str, command_list):
        super().__init__(header, command_list)
        self.__book = Book()

    def handle_input(self, state_manager):
        user_input = ui.get_input()

        if user_input == Actions.SetTitle.value:
            value = ui.get_single_input()
            self.set_title(value)
            state_manager.change_state(self)
        elif user_input == Actions.SetAuthor.value:
            value = ui.get_single_input()
            self.set_author(value)
            state_manager.change_state(self)
        elif user_input == Actions.SetYear.value:
            value = ui.get_single_input()
            self.set_year(value)
            state_manager.change_state(self)
        elif user_input == Actions.Execute.value:
            self.execute(state_manager)
            state_manager.change_state(self)
        elif user_input == Actions.Back.value:
            self.clear_book()
            state_manager.change_state(States.Main)
        else:
            print("Ошибка ввода. Повторите попытку")
            pass

    def set_title(self, title: str):
        self.__book.title = title
        print(f"Значение %s установлено", title)

    def set_author(self, author: str):
        self.__book.author = author
        print(f"Значение %s установлено", author)

    def set_year(self, year: int):
        self.__book.year = year
        print(f"Значение %s установлено", year)

    def execute(self, state_manager):
        state_manager.book_rep.add(self.__book)
        self.clear_book()
        print("Книга добавлена")

    def clear_book(self):
        self.__book = Book()


class RemoveBookState(State):
    def handle_input(self, state_manager):
        user_input = ui.get_input()

        if user_input == Actions.Back.value:
            state_manager.change_state(States.Main)
        else:
            try:
                state_manager.book_rep.remove_at(user_input)
                print("Книга успешно удалена")
                state_manager.change_state(States.Main)
            except:
                print("Ошибка при попытке удалить книгу. Попробуйте еще раз")


class StateManager:
    def __init__(self, book_rep: BookRep):
        self.state_changed = Event()
        self.__current_state = States.Main
        self.book_rep = book_rep
        self.is_work = True

    @property
    def current_state(self):
        return self.__current_state

    def stop_work(self):
        self.is_work = False

    def change_state(self, state: State):
        self.__current_state = state
        ui.clear()
        string_state = self.__current_state.to_string(self)
        self.state_changed.invoke(string_state)


class States:
    Main = MainState(f'Сейчас в библиотеке %s книг.', [
        Command(Actions.Exit, "выхода"),
        Command(Actions.AddBook, "добавления книги"),
        Command(Actions.RemoveBook, "удаления книги"),
        Command(Actions.FindBook, "поиска книги"),
        Command(Actions.PrintAt, "вывода детальной информации о книге"),
        Command(Actions.PrintAll, "вывода всех книг")
    ])

    AddBook = AddBookState(f'Вы пытаетесь добавить книгу.', [
        Command(Actions.SetTitle, "установки название книги"),
        Command(Actions.SetAuthor, "установки автора книги"),
        Command(Actions.SetYear, "установки года издания книги"),
        Command(Actions.Execute, "выполнения команды"),
        Command(Actions.Undo, "отмены"),
    ])

    RemoveBook = RemoveBookState(f'Введите id книги для удаления.', [
        Command(Actions.Back, "для выхода из меню добавления"),
    ])

    PrintAll = PrintAllState(f'Сейчас в библиотеке %s книг.', [
        Command(Actions.Return, "отмены")
    ])

    Exit = ExitState(f'Сейчас в библиотеке %s книг. Выход из библиотеки.', [])
