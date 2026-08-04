class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def __init__(self):
        pass

    def teach(self):
        print("Mentor teaches")

    def groom(self):
        print("Mentor grooms")
        
    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")

    def mark_borrowed(self):
        self.is_available = False
        print(f"{self.title} has been marked as borrowed.")


book1 = Book("1984", "George Orwell", True)

book1.display_info()
book1.mark_borrowed()
book1.display_info()