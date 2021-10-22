import csv
import json


def get_books(filepath):
    """Читает файл с информацией о книгах"""
    book_fields = ('title', 'author', 'pages', 'genre')
    with open(filepath) as file:
        reader = csv.DictReader(file)
        books = [{key.lower(): value for key, value in book.items() if key.lower() in book_fields} for book in reader]
    return books


def get_users(filepath):
    """Читает файл с информацией о пользователях"""
    with open(filepath) as file:
        users = json.load(file)
    return users


def get_users_main_info(users):
    """Представляет информацию о юзерах согласно референсу"""
    users = [
        {
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': []
        } for user in users]
    return users


def distribute_books(users_list, books_list):
    """Распределяет книги между пользователями"""
    users = get_users_main_info(users_list)
    books = books_list.copy()
    while books:
        for user in users:
            if not books:
                break
            user['books'].append(books.pop())
    return users


def write_result(data, filepath='result.json'):
    """Записывает результат в файл"""
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    books_l = get_books('books.csv')
    users_l = get_users('users.json')
    users_with_books = distribute_books(users_l, books_l)
    write_result(users_with_books)
