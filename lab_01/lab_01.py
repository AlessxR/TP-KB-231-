import operator

# Список студентів
students = [
    {"name": "Bob", "phone": "0641234567", "surname": "Litvinenko", "course": "4"},
    {"name": "Emma", "phone": "0651234567", "surname": "Ilyenko", "course": "1"},
    {"name": "Jon", "phone": "0661234567", "surname": "Kotsyuba", "course": "4"},
    {"name": "Zak", "phone": "0671234567", "surname": "Starodub", "course": "3"}
]

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
    """Функція для додавання нового елементу до списку студентів."""
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    surname = input("Please enter student surname: ")
    course = input("Please enter student course: ")
    new_item = {"name": name, "phone": phone, "surname": surname, "course": course}

    insert_position = 0
    for item in students:
        if name > item["name"]:
            insert_position += 1
        else:
            break
    students.insert(insert_position, new_item)
    print("New element has been added.")

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
    """Функція для оновлення інформації про студента у списку."""
    print_all_list()
    name_to_update = input("Please enter the name of the student to be updated: ")
    phone_to_update = input("Please enter the phone of the student to be updated: ")

    for student in students:
        if student["name"].lower() == name_to_update.lower() and student["phone"] == phone_to_update:
            print(f"Updating information for {student['name']}")

            new_name = input(f"Please enter new name (or press Enter to keep '{student['name']}'): ")
            new_phone = input(f"Please enter new phone (or press Enter to keep '{student['phone']}'): ")
            new_surname = input(f"Please enter new surname (or press Enter to keep '{student['surname']}'): ")
            new_course = input(f"Please enter new course (or press Enter to keep '{student['course']}'): ")

            student["name"] = new_name if new_name else student["name"]
            student["phone"] = new_phone if new_phone else student["phone"]
            student["surname"] = new_surname if new_surname else student["surname"]
            student["course"] = new_course if new_course else student["course"]

            students.sort(key=operator.itemgetter("name"))
            print("Student information updated and list sorted.")
            break
    else:
        print("Student not found.")

def main():
    """Головна функція, яка організовує взаємодію з користувачем."""
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
                print("Exit")
                break
            case _:
                print("Wrong choice")

main()
