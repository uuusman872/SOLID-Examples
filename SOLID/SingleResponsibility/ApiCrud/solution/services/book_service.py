
from repos.books_repo import BookRepo
from models.BookModel import Book
from fastapi import HTTPException


class BookService:
    def __init__(self, repo: BookRepo):
        self.repo = repo

    def create_book(self, book: Book):
        if self.repo.get_by_id(book.id):
            raise HTTPException(status_code=400, detail="Book already exist's")
        book = self.repo.create(book)
        return book

    def borrow_book(self, book_id: int):
        book = self.repo.get_by_id(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        elif book.is_borrowed:
            raise HTTPException(status_code=400, detail="Book is already borrowed")
        book.is_borrowed = True
        return book
    
    def return_book(self, book_id: int):
        book = self.repo.get_by_id(book_id)
        if not book:
            raise HTTPException(status_code=400, detail="Book not found")
        book.is_borrowed = False
        return book
    
    