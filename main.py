from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass
    

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError("Довжина номеру повинна = 10")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone_str):
        if phone_str:
            self.phones.append(Phone(phone_str))

    def edit_phone(self, old_phone, new_phone):
        # перевірка чи введений номер телефону знаходиться в списку
        if old_phone not in [phone.value for phone in self.phones]:
            raise ValueError("Old phone not exist")
        else:
            # в іншому випадку проходимось по всіх елементах і змінюємо старий на новий
            self.phones = [phone if phone.value != old_phone else Phone(new_phone) for phone in self.phones]

    def find_phone(self, find_phone):
        # пошук 
        for phone in self.phones:
            if phone.value == find_phone:
                return phone
        return None

    def remove_phone(self, str_phone):
        # перевірка чи введений номер телефону знаходиться в списку
        if str_phone not in [phone.value for phone in self.phones]:
            raise ValueError("Phone not exist")
        else:
            self.phones.remove(self.find_phone(str_phone))
            

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        # додаємо значення до власного списку
        self.data[record.name.value] = record

    def find(self, args):
        # пошук 
        return self.data[args]

    def delete(self, name):
        # видалення
        del self.data[name]

    def __str__(self):
        # створюємо рядок для красивого виведення 
        returning = "--------- Address book ---------\n"
        for line in self.data.values():
            returning += f"{line}\n"
        returning += "--------------------------------"
        return returning
def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")


if __name__ == '__main__':
    main()