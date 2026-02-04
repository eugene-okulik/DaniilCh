from task_1 import Book


class SchoolBook(Book):
    def __init__(
            self, title, author, pages, isbn, subject, school_grade, has_tasks
    ):
        super().__init__(title, author, pages, isbn)
        self.subject = subject
        self.school_grade = school_grade
        self.has_tasks = has_tasks

    def print_info(self):
        if self.is_reserved:
            print(
                f"Название: {self.title}, Автор: {self.author}, "
                f"страниц: {self.pages}, предмет: {self.subject}, "
                f"класс: {self.school_grade}, зарезервирована"
            )
        else:
            print(
                f"Название: {self.title}, Автор: {self.author}, "
                f"страниц: {self.pages}, предмет: {self.subject}, "
                f"класс: {self.school_grade}"
            )


book1 = SchoolBook(
    "Алгебра", "Иванов", 200, "111-222", "Математика", 9, True
)
book2 = SchoolBook(
    "История", "Петров", 180, "333-444", "История", 8, False
)
book3 = SchoolBook(
    "География", "Сидоров", 220, "555-666", "География", 7, True
)

book2.reserve()

for book in [book1, book2, book3]:
    book.print_info()
