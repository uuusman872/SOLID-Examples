from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False
        self.book_lost = False
        self.book_fine = 200
        self.borrower = None
        self.due_date = None
        self.reviews = []


class BookLostHandler:
    def mark_as_lost(self, book: Book):
        book.book_lost = True
        return book


class BookOverdueHandler:    
    def get_overdue_books(self, user, books: list[Book]):
        overdue_books = []
        for book in books:
            if book.borrower == user and book.due_date and book.due_date < datetime.now():
                overdue_books.append(book)
        return overdue_books


class BookCirculationHandler:
    def borrow(self, book: Book, user, days=14):
        if not book.is_borrowed:
            book.is_borrowed = True
            book.borrower = user
            book.due_date = datetime.now() + timedelta(days=days)
            print(f"{user} borrowed {book.title} (due {book.due_date.date()})")
        else:
            print(f"{book.title} is already borrowed")
    
    def return_book(self, book: Book, user):
        if book.is_borrowed:
            book.is_borrowed = False
            book.borrower = None
            book.due_date = None
            print(f"{user} returned {book.title}")
        else:
            print(f"{book.title} was not borrowed")

    def extend_borrow_period(self, book: Book, extra_days):
        if book.is_borrowed and book.due_date:
            book.due_date += timedelta(days=extra_days)
        return book


class ReviewManagerHandler:
    def add_review(self, book: Book, user, review):
        book.reviews.append({"user": user, "review": review})
        return book

    def get_reviews(self, book: Book):
        return book.reviews


class ReadingTimeCalculator:
    def calculate_reading_time(self, book: Book, pages_per_hour=30):
        return book.pages // pages_per_hour

    def calculate_fine(self, book: Book):
        if book.due_date and datetime.now() > book.due_date:
            days_overdue = (datetime.now() - book.due_date).days
            return book.book_fine * days_overdue
        return 0
