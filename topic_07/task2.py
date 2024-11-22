class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [
    Student("Oleksadr", 18),
    Student("Alice", 19),
    Student("Bob", 20),
    Student("Oblen", 16)
]

sorted_students = sorted(students, key=lambda student: student.age)

# Виведення відсортованих студентів
for student in sorted_students:
    print(f"Name: {student.name}, Age: {student.age}")
