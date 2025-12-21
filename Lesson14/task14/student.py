from Lesson14.task14.human import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {super().__str__()}, record No: {self.record_book}'

    def __eq__(self, student):
        return str(self) == str(student)

    def __hash__(self):
        return hash(str(self))
