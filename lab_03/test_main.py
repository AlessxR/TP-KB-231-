import pytest
from Student import Student
from StudentList import StudentList

def test_add_student():
    sl = StudentList()
    student = Student("Alice", "123", "Brown", "1")
    sl.add_student(student)
    assert len(sl.students) == 1
    assert sl.students[0].name == "Alice"

def test_delete_student():
    sl = StudentList()
    student = Student("Alice", "123", "Brown", "1")
    sl.add_student(student)
    sl.delete_student("Alice", "123")
    assert len(sl.students) == 0

def test_update_student():
    sl = StudentList()
    student = Student("Alice", "123", "Brown", "1")
    sl.add_student(student)
    updated_student = Student("Alice", "123", "Green", "2")
    sl.update_student("Alice", "123", updated_student)
    assert sl.students[0].surname == "Green"
    assert sl.students[0].course == "2"
