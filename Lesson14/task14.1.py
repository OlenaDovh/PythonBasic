"""
Модифікуйте клас Група (завдання минулої лекції) так,
щоб при спробі додавання до групи більше 10-ти студентів, було порушено виняток користувача.
Таким чином потрібно створити ще й виняток користувача для цієї ситуації.
І обробити його поза межами класу. Тобто. потрібно перехопити цей виняток, при спробі додавання 11-го студента
"""
import random

class CustomError(Exception):
    pass

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} of {self.age} years old is {self.gender}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {super().__str__()}, record No: {self.record_book}'

class Group:

    def __init__(self, number, max_st_cnt = 10):
        self.number = number
        self.group = set()
        self.max_st_cnt = max_st_cnt

    def add_student(self, student):
        if len(self.group) >= self.max_st_cnt:
            raise CustomError("The group is full. You can't add more students.")
        self.group.add(student)
        print(student)

    def delete_student(self, last_name):
        searched_student = self.find_student(last_name)
        self.group.discard(searched_student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        ...
        return f'Number:{self.number}\\n {all_students} '

gr = Group('PD1')

first_names = ["Ivan", "Vlad", "Michael", "Oleh", "Olha", "Iryna", "Natalia", "Olena"]
last_names = ["Dudar", "Shevchenko", "Bondar", "Tkachenko", "Melnyk", "Savchuk", "Lysenko"]
genders = ["Male", "Female"]

def random_student():
    gender = random.choice(genders)
    age = random.randint(18, 30)
    first = random.choice(first_names)
    last = random.choice(last_names)
    record_book = f"AN{random.randint(100, 999)}"
    return Student(gender, age, first, last, record_book)

try:
    for i in range(11):
        gr.add_student(random_student())
except CustomError as err:
    print(err)