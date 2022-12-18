def main_menu():
    print('\nВыберите пункт меню')
    print('1. Показать телефонную книгу')
    print('2. Открыть файл телефонной книги')
    print('3. Сохранить файл электронной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выход\n')
    return choice_main_menu()

def choice_main_menu():
   while True:
       try:
           choice = int(input('Выберите пункт меню'))
           if choice in range(0, 8):
               return choice
           else:
               print('Такого пункта нет, повторите попытку')
       except:
             print('Ошибка ввода! Некорректные данные!')

def print_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    else:
        print('Телефонная книга пуста или не загружена')

def log_off():
    print('До свидания, до новых встреч!')

def input_new_book():
    name = input('Введите имя')
    phone = input('Введите номер телефона')
    comment = print('Введите комментарий')
    return[name, phone, comment]

def log_success():
    print('Телефонная книга загружена')

def save_success():
    print('Контакт удален')

def input_remove_contact():
    id = int(input('В'))
