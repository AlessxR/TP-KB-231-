import operator
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
students = [
    {"name":"Bob", "phone":"0641234567", "surname":"Litvinenko", "course":"4"},
    {"name":"Emma", "phone":"0651234567", "surname":"Ilyenko","course":"1"},
    {"name":"Jon",  "phone":"0661234567", "surname":"Kotsyuba", "course":"4"},
    {"name":"Zak",  "phone":"0671234567", "surname":"Starodub", "course":"3"}
]

def printAllList():
    for elem in students:
        strForPrint = (
            "Student name is " + elem["name"] +
            ", Phone is " + elem["phone"] +
            ", surname is " + elem["surname"] +
            ", Course is " + elem["course"]
        )
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    surname = input("Please enter student surname: ")
    course = input("Please enter student course: ")
    newItem = {"name": name, "phone": phone, "surname": surname, "course": course}
    
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    phone = input("Please enter phone to be deleted: ")
    deletePosition = -1
    for i, item in enumerate(students):
        if name == item["name"] and phone == item["phone"]:
            deletePosition = i
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del students[deletePosition]  # видаляємо по знайденному індексу
    return



def updateElement():
    printAllList()  # Весь список перед оновленням
    name_to_update = input("Please enter the name of the student to be updated: ")  # Меседж для вводу імені студента, який потрібно апдейднути
    phone_to_update = input("Please enter the phone of the student to be updated: ")

    # Пошук студента з таким ім'ям
    for student in students:
        if student["name"].lower() == name_to_update.lower() and student["phone"] == phone_to_update:  # 
            print(f"Updating information for {student['name']}")
            
            
            new_name = input(f"Please enter new name (or press Enter to keep '{student['name']}'): ")
            new_phone = input(f"Please enter new phone (or press Enter to keep '{student['phone']}'): ")
            new_surname = input(f"Please enter new surname (or press Enter to keep '{student['surname']}'): ")
            new_course = input(f"Please enter new course (or press Enter to keep '{student['course']}'): ")

            
            student["name"] = new_name if new_name else student["name"]
            student["phone"] = new_phone if new_phone else student["phone"]
            student["surname"] = new_surname if new_surname else student["surname"]
            student["course"] = new_course if new_course else student["course"]
            
            
            students.sort(key=operator.itemgetter("name")) # сортування за допомогою itemgetter по "name"

            print("Student information updated and list sorted.")
            
            break
    else:
        print("Student not found.")



def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()