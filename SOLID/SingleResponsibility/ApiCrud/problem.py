from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


# ===== MODELS =====
class Book(BaseModel):
    id: int
    title: str
    author: str
    pages: int
    is_borrowed: bool = False

# ===== IN-MEMORY DB =====
books: List[Book] = []

# ===== GOD-CLASS STYLE API (no SRP) =====


@app.post("/books")
def create_book(book: Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book already exists")
    books.append(book)
    return {"message": "Book created", "book": book}


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return {"message": "Book updated", "book": updated_book}
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            deleted = books.pop(i)
            return {"message": "Book deleted", "book": deleted}
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books/{book_id}/borrow")
def borrow_book(book_id: int):
    for book in books:
        if book.id == book_id:
            if book.is_borrowed:
                raise HTTPException(status_code=400, detail="Book already borrowed")
            book.is_borrowed = True
            return {"message": f"{book.title} has been borrowed"}
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books/{book_id}/return")
def return_book(book_id: int):
    for book in books:
        if book.id == book_id:
            if not book.is_borrowed:
                raise HTTPException(status_code=400, detail="Book was not borrowed")
            book.is_borrowed = False
            return {"message": f"{book.title} has been returned"}
    raise HTTPException(status_code=404, detail="Book not found")