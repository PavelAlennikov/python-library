from model.book import Book


class BookFormatter:

    @staticmethod
    def format_books(books):
        book_list = ''
        index = 1

        for book in books:
            book_list += f'{index} - {BookFormatter.format_book(book)}\n'
            index += 1

        return book_list

    @staticmethod
    def format_book(book: Book):
        return f'{book[0]}, {book[1].title}, {book[1].year}, {book[1].author}'
