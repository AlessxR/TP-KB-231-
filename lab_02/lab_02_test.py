import pytest
from lab_02 import add_new_element, update_element, delete_element, print_all_list, students
import pytest
from lab_02 import add_new_element, update_element, delete_element, students

def test_add_new_element(monkeypatch):
    # Дані для нового студента
    inputs = iter(["Oleksandr", "0681234567", "Kravchuk", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Перевірка довжини до і після додавання
    initial_len = len(students)
    add_new_element()
    assert len(students) == initial_len + 1
    assert any(student["name"] == "Oleksandr" and student["phone"] == "0681234567" for student in students)

def test_update_element(monkeypatch):
    # Спочатку додаємо студента, щоб було кого оновлювати
    students.append({"name": "Oleksandr", "phone": "0681234567", "surname": "Kravchuk", "course": "3"})

    # Дані для оновлення студента
    inputs = iter(["Oleksandr", "0681234567", "Oleksii", "0689876543", "Kravchenko", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Оновлення
    update_element()

    # Перевірка, чи оновлені дані студента
    updated_student = next(student for student in students if student["name"] == "Oleksii")
    assert updated_student["phone"] == "0689876543"
    assert updated_student["surname"] == "Kravchenko"
    assert updated_student["course"] == "4"

def test_delete_element(monkeypatch):
    # Спочатку додаємо студента для видалення
    students.append({"name": "Oleksandr", "phone": "0681234567", "surname": "Kravchuk", "course": "3"})

    # Дані для видалення
    inputs = iter(["Oleksandr", "0681234567"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Перевірка довжини до і після видалення
    initial_len = len(students)
    delete_element()
    assert len(students) == initial_len - 1
    assert not any(student["name"] == "Oleksandr" and student["phone"] == "0681234567" for student in students)
