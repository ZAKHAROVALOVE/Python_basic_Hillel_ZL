import zipfile
import os

def create_zip():
    with zipfile.ZipFile('student_group.zip', 'w') as zipf:
        for file in ['human.py', 'student.py', 'group.py', 'main.py']:
            zipf.write(file)
        print('student_group.zip created successfully.')

if __name__ == "__main__":
    create_zip()
