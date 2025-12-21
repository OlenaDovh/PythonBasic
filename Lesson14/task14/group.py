from Lesson14.task14.custom_error import CustomError


class Group:

    def __init__(self, number, max_st_cnt = 10):
        self.number = number
        self.group = set()
        self.max_st_cnt = max_st_cnt

    def add_student(self, student):
        if len(self.group) >= self.max_st_cnt:
            raise CustomError("The group is full. You can't add more students.")
        self.group.add(student)

    def delete_student(self, last_name):
        searched_student = self.find_student(last_name)
        self.group.discard(searched_student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(st) for st in self.group)
        return f'Number:{self.number} \n{all_students} '