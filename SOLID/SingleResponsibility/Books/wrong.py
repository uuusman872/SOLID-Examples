class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False

    def borrow(self, user):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{user} borrowed {self.title}")
        else:
            print(f"{self.title} is already borrowed")

    def return_book(self, user):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{user} returned {self.title}")
        else:
            print(f"{self.title} was not borrowed")

    def calculate_reading_time(self):
        return self.pages // 30  # assume 30 pages/hour
