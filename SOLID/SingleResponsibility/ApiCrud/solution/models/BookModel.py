from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    pages: int
    is_borrowed: bool = False

    