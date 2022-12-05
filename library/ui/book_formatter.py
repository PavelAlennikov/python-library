from model.book import Book


class BookFormatter:

    @staticmethod
    def format_books(books):
        book_list = ''
        index = 1

        for book in books:
            book_list += f'{index} - {book}\n'
            index += 1

        return book_list

    @staticmethod
    def format_book(book: Book):
        return book.__str__()
