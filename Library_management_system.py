class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_available = True

    def get_status(self):
        return "Доступна" if self._is_available else "Видана"

    def __str__(self):
        return f"'{self.title}' ({self.author}) — {self.get_status()}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_status(self):
        status = super().get_status()
        return f"{status} (електронна)"


class Library:
    def __init__(self):
        self._books = []

    def __len__(self):
        return len(self._books)  # кількість книг

    def __eq__(self, other):
        return len(self._books) == len(other._books)  # чи однакові бібліотеки

    def add_book(self, book):
        self._books.append(book)

    def borrow_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_available:
                    book._is_available = False
                    print(f"Ви взяли книгу: {title}")
                    return
                else:
                    print(f"Книга '{title}' недоступна (вже видана).")
                    return
        print(f"Книгу '{title}' не знайдено в бібліотеці.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_available = True
                print(f"Ви повернули книгу: {title}")
                return
        print(f"Цієї книги немає в нашому обліку.")

    def show_all(self):
        print("\n--- Список книг у бібліотеці ---")
        for book in self._books:
            print(book)
        print("--------------------------------\n")


# --- Демонстрація роботи ---

# Створюємо бібліотеку
my_library = Library()
my_library2 = Library()

# Додаємо 2 звичайні книги і 1 електронну
my_library.add_book(Book("Кобзар", "Тарас Шевченко"))
my_library.add_book(Book("1984", "Джордж Орвелл"))
my_library.add_book(EBook("Чистий код", "Роберт Мартін", 5.2))

# Показуємо початковий стан
my_library.show_all()

# Спроба взяти книгу
my_library.borrow_book("1984")

# Спроба взяти ту саму книгу ще раз
my_library.borrow_book("1984")

# Показуємо стан після видачі
my_library.show_all()

# Повернення книги
my_library.return_book("1984")

# Фінальний стан
my_library.show_all()

print(len(my_library))
print(len(my_library2))
print(my_library == my_library2)

# Версія 1.0
print("Бібліотека запущена!")