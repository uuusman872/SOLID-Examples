from fastapi import APIRouter
from services.book_service import BookService
from repos.books_repo import BookRepo
from models.BookModel import Book

router = APIRouter(prefix="books", tags=["books"])


book_repo = BookRepo()
service = BookService(repo=book_repo)

@router.post("/")
async def create_book(book: Book):
    book = service.create_book(book)
    return book

@router.get("/books")
def list_books():
    return book_repo.get_all()


@router.post("/books/{book_id}/borrow")
def borrow_book(book_id: int):
    return service.borrow_book(book_id)


@router.post("/books/{book_id}/return")
def return_book(book_id: int):
    return service.return_book(book_id)
