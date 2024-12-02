from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        """Додає нового студента до списку (в алфавітному порядку за іменем)."""
        self.students.append(student)
        self.students.sort(key=lambda s: s.name.lower())

    def delete_student(self, name: str, phone: str):
        """Видаляє студента зі списку."""
        self.students = [s for s in self.students if not (s.name == name and s.phone == phone)]

    def update_student(self, name: str, phone: str, updated_student: Student):
        """Оновлює інформацію про студента."""
        for i, student in enumerate(self.students):
            if student.name == name and student.phone == phone:
                self.students[i] = updated_student
                self.students.sort(key=lambda s: s.name.lower())
                return
        print("Student not found.")

    def print_all(self):
        """Виводить список студентів."""
        for student in self.students:
            print(student)

    def to_dict_list(self):
        """Перетворює список студентів у формат списку словників."""
        return [s.to_dict() for s in self.students]
