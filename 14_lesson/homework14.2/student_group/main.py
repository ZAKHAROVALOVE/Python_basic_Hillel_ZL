from student import Student
from group import Group

if __name__ == "__main__":
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)

    print(gr)

    assert gr.find_student('Jobs') == st1, 'Тест 1'
    assert gr.find_student('Jobs2') is None, 'Тест 2'
    assert isinstance(gr.find_student('Jobs'), Student), 'Метод пошуку повинен повертати екземпляр класу'

    gr.delete_student('Taylor')
    print(gr)  # Лише один студент

    gr.delete_student('Taylor')  # Не буде помилки (студент вже видалений)
