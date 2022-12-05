from fpdf import FPDF
from ui.book_formatter import BookFormatter

from model.book import Book


class PdfPrinter:

    @staticmethod
    def print_book(file_name: str, book: Book):
        book_text = BookFormatter.format_book(book)
        pdf = PdfPrinter.__create_pdf()
        pdf.cell(250, 30, "Your book:", ln=1, align="L")
        pdf.cell(250, 15, book_text, ln=1, align="L")
        pdf.output(file_name)

    @staticmethod
    def print_books(file_name: str, books):
        pdf = PdfPrinter.__create_pdf()
        pdf.cell(250, 30, "Your library:", ln=1, align="L")
        index = 0
        for book in books:
            index = index + 1
            book_text = BookFormatter.format_book(book)
            pdf.cell(250, 15, f'{index} - {book_text}', ln=1, align="L")
        pdf.output(file_name)

    @staticmethod
    def __create_pdf():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=16)

        return pdf
