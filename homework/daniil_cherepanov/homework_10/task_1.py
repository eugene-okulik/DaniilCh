class Book:
    material = "бумага"
    has_text = True

    def __init__(self, title, author, pages, isbn):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = False

    def reserve(self):
        self.is_reserved = True

    def print_info(self):
        if self.is_reserved:
            print(
                f"Название: {self.title}, Автор: {self.author}, "
                f"страниц: {self.pages}, материал: {self.material}, "
                f"зарезервирована"
            )
        else:
            print(
                f"Название: {self.title}, Автор: {self.author}, "
                f"страниц: {self.pages}, материал: {self.material}"
            )


# Создаём экземпляры книг
book1 = Book("Идиот", "Достоевский", 500, "123-456")
book2 = Book("Капитанская дочка", "Пушкин", 450, "789-101")
book3 = Book("Тринадцатый подвиг Геракла", "Искадер", 1300, "112-131")
book4 = Book("Мастер и Маргарита", "Булгаков", 380, "415-161")
book5 = Book("Тихий Дон", "Шолохов", 320, "718-192")

book3.reserve()

for book in [book1, book2, book3, book4, book5]:
    book.print_info()
