phone_book = []

def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book

def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)

def remove_contact(id):
    global phone_book
    name = phone_book[id-1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}? (y/n) ')
    if confirm.lower() == 'y':
        phone_book.pop(id-1)
        return True
    return False

def replace_contact(id, contact):
    global phone_book
    name = phone_book[id-1][0]
    confirm = input(f'Вы действительно хотите изменить контакт {name} на {contact[0]}? (y/n) ')
    if confirm.lower() == 'y':
        phone_book[id-1] = contact
        return True
    return False

def find_contact(text):
    global phone_book
    new_phone_book = []
    for contact in phone_book:
        for i in range(len(contact)):
            if text in contact[i]:  # текст содержится в элементe контакта
                new_phone_book.append(contact)
                break
    return new_phone_book

# def del_contact(new_phone_book):