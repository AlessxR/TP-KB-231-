import operator
import sys
import csv

# Список студентів
students = [{"name": "Bob", "phone": "0641234567", "surname": "Litvinenko", "course": "4"},
        {"name": "Emma", "phone": "0651234567", "surname": "Ilyenko", "course": "1"},
        {"name": "Jon", "phone": "0661234567", "surname": "Kotsyuba", "course": "4"},
        {"name": "Zak", "phone": "0671234567", "surname": "Starodub", "course": "3"}]

def loadFromCsv(filename):
    global students
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            students = sorted(reader, key=lambda x: x['name'].lower())
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except IOError:
        print(f"Error: Could not read the file {filename}.")

def saveToCsv(filename):
    global students
    try:
        with open(filename, mode="w", newline='', encoding="utf-8") as csvfile:
            fieldnames = ['name', 'phone', 'surname', 'course']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow(student)
    except IOError:
        print(f"Error: Could not write to the file {filename}.")

def print_all_list():
    """Функція для виведення всього списку студентів."""
    for elem in students:
        str_for_print = (
            f"Student name is {elem['name']}, "
            f"Phone is {elem['phone']}, "
            f"surname is {elem['surname']}, "
            f"Course is {elem['course']}"
        )
        print(str_for_print)

def add_new_element():
    """Функція для додавання нового студента у відсортоване положення списку."""
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    surname = input("Please enter student surname: ")
    course = input("Please enter student course: ")
    new_item = {"name": name, "phone": phone, "surname": surname, "course": course}

    insert_position = next((i for i, item in enumerate(students) if name < item["name"]), len(students))
    students.insert(insert_position, new_item)
    print("New student added.")

def delete_element():
    """Функція для видалення елементу зі списку студентів."""
    name = input("Please enter name to be deleted: ")
    phone = input("Please enter phone to be deleted: ")
    delete_position = -1
    for i, item in enumerate(students):
        if name == item["name"] and phone == item["phone"]:
            delete_position = i
            break
    if delete_position == -1:
        print("Element was not found.")
    else:
        del students[delete_position]
        print("Element has been deleted.")

def update_element():
    """Функція для оновлення інформації про студента у відсортованому списку."""
    name = input("Please enter the name of the student to update: ")
    phone = input("Please enter the phone of the student to update: ")

    for i, student in enumerate(students):
        if student["name"].lower() == name.lower() and student["phone"] == phone:
            print(f"Updating information for {student['name']}")

            new_name = input(f"New name (Enter to keep '{student['name']}'): ") or student["name"]
            new_phone = input(f"New phone (Enter to keep '{student['phone']}'): ") or student["phone"]
            new_surname = input(f"New surname (Enter to keep '{student['surname']}'): ") or student["surname"]
            new_course = input(f"New course (Enter to keep '{student['course']}'): ") or student["course"]

            # Видаляємо старий запис і додаємо новий у відсортоване положення
            del students[i]
            new_student = {"name": new_name, "phone": new_phone, "surname": new_surname, "course": new_course}
            
            # Знаходимо індекс для нової позиції студента
            insert_position = len(students)  #  елемент буде в кінці списку
            for j, item in enumerate(students):
                if new_name < item["name"]:
                    insert_position = j
                    break

            # Вставляємо нового студента в обчислену позицію
            students.insert(insert_position, new_student)
            print("Student information updated and placed in sorted position.")
            return
    print("Student not found.")


def main(filename):
    """Головна функція, яка організовує взаємодію з користувачем."""
    loadFromCsv(filename)
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        match choice.lower():
            case "c":
                print("New element will be created:")
                add_new_element()
                print_all_list()
            case "u":
                print("Existing element will be updated")
                update_element()
                print_all_list()
            case "d":
                print("Element will be deleted")
                delete_element()
            case "p":
                print("List will be printed")
                print_all_list()
            case "x":
                print("Exit...")
                saveToCsv(filename)
                break
            case _:
                print("Wrong choice")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        main(sys.argv[1])
