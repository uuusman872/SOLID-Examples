from typing import List
from models.BookModel import Book


class BookRepo:
    def __init__(self):
        self.books: List[Book] = []
    
    def create(self, book: Book):
        self.books.append(Book)
        return book
    
    def get_all(self):
        return self.books


    def get_by_id(self, id):
        return next((book for book in self.books if book.id == id), None)


    def update(self, book_id: int, updated_book: Book):
        for i,  book in self.books:
            if book.id == book_id:
                self.books[i] = updated_book
                return updated_book
        return None
    
    def delete(self, book_id): 
        for i, book in self.books:
            if book.id == book_id:
                return self.books.pop(i)
        return None

            
    
    
