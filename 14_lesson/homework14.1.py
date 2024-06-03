from typing import Optional


class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"Student: {self.gender}, {self.age}, {self.first_name}, {self.last_name}, {self.record_book}"


class GroupLimitError(Exception):
    """Під час додавання до групи більше ніж 10 студентів виникає спеціальний виняток."""
    pass


class Group:
    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= 10:
            raise GroupLimitError(f"Неможливо додати студента {student.first_name} {student.last_name}: група повна")
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


if __name__ == "__main__":
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr = Group('gr')

    try:
        gr.add_student(st2)
        gr.add_student(st1)
        # Adding more students to test the exception
        for i in range(3, 12):
            gr.add_student(Student('Female', 22, f'Student{i}', f'Last{i}', f'AN14{i}'))
    except GroupLimitError as e:
        print(e)

    print(gr) # Перше виведення групи, після додавання всіх студентів

    assert str(gr.find_student('Jobs')) == str(st1), 'Тест 1'
    assert gr.find_student('Jobs2') is None, 'Тест 2'
    assert isinstance(gr.find_student('Jobs'), Student), 'Метод пошуку повинен повертати екземпляр класу'

    gr.delete_student('Taylor')
    print(gr)  # Лише один студент, після видалення 'Taylor'

    gr.delete_student('Taylor')  # Не буде помилки (студент вже видалений)
