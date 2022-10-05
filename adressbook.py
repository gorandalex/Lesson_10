from collections import UserDict


class AdressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

class Record():
    def __init__(self, name, phone = None):
        self.name = name
        self.phone = []
        if phone:
            self.phone.append(phone)

    def add_phone(self, phone):
        self.phone.append(phone)
    
    def delete_phone(self, phone):
        if phone in self.phone:
            self.phone.remove(phone)

    def change_phone(self, old_phone, new_phone):
        if old_phone in self.phone:
            self.phone[self.phone.index(old_phone)] = new_phone

class Field():
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass
