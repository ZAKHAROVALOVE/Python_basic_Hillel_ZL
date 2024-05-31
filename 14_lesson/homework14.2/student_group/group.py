from typing import Optional
from student import Student

class Group:
    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str) -> Optional[Student]:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        sorted_students = sorted(self.group, key=lambda student: student.last_name)
        all_students = "\n".join(str(student) for student in sorted_students)
        return f"Number: {self.number}\n{all_students}"
