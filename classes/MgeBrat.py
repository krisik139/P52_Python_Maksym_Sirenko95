#class Book:
#    def __init__(self, title, author):
#        self.title = title
#        self.author = author
#
#    def info(self):
#        print(f"{self.title}, автор: {self.author}")
#
#
#class Reader:
#    def __init__(self, name):
#        self.name = name
#        self.book = None
#
#    def take_book(self, book):
#        self.book = book
#        print(f"{self.name} взяв(ла) книгу: {self.book.title}")
#
#    def show_book(self):
#        if self.book is None:
#            print(f"{self.name} зараз без книги")
#
#        else:
#            print(f"{self.name} читає книгу")
#
#
#book1 = Book("Мистецтво програмування", "Дональд Кнут")
#reader1 = Reader("Максим")
#
#reader1.show_book()
#reader1.take_book(book1)
#reader1.show_book()

class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def info(self):
        print(f"Фільм: {self.title} - {self.duration} хв.")


class CinemaHall:
    def __init__(self):
        self.current_movie = None

    def start_movie(self, movie):
        self.current_movie = movie
        print(f"Починаємо показ фільму: {self.current_movie.title}")

    def show_movie(self):
        if not self.current_movie is None:
            print(f"У залі проходить показ ''{self.current_movie.title}''")
        else:
            print(f"У залі нічого поки що не показується.")


first_movie = Movie("Помста МГЕ брата(14+)", 26)
first_movie.info()
second_movie = Movie("Червоний слоник(3+)",80)
second_movie.info()

live_room = CinemaHall()
live_room.show_movie()
live_room.start_movie(first_movie)
live_room.show_movie()
live_room.start_movie(second_movie)
live_room.show_movie()


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def info(self):
        print(f"Ім'я: {self.name}; Телефон: {self.phone}")
class Phone:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Успішно добавлено! {self.contacts[-1].phone}")

    def show_all(self):
        if len(self.contacts) > 0:
            for contact in self.contacts:
                contact.info()

_1 = Contact("Назар", 380962013456)
_2 = Contact("Даніела", 380962083412)
_3 = Contact("Микола", 380969013735)

# Я не буду дубаситися і покажу весь функціонал як людина
phone = Phone()
phone.show_all()
phone.add_contact(_1)
phone.add_contact(_2)
phone.add_contact(_3)
phone.show_all()