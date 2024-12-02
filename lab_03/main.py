import sys
from Student import Student
from StudentList import StudentList
from FileManager import FileManager

def main(filename):
    student_list = FileManager.load_from_csv(filename)

    while True:
        choice = input("Choose action [C create, U update, D delete, P print, X exit]: ").lower()
        match choice:
            case "c":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                surname = input("Enter surname: ")
                course = input("Enter course: ")
                student = Student(name, phone, surname, course)
                student_list.add_student(student)
                print("Student added.")
            case "u":
                name = input("Enter name of student to update: ")
                phone = input("Enter phone: ")
                print("Enter new data:")
                new_name = input("Name: ")
                new_phone = input("Phone: ")
                new_surname = input("Surname: ")
                new_course = input("Course: ")
                updated_student = Student(new_name, new_phone, new_surname, new_course)
                student_list.update_student(name, phone, updated_student)
            case "d":
                name = input("Enter name of student to delete: ")
                phone = input("Enter phone: ")
                student_list.delete_student(name, phone)
                print("Student deleted.")
            case "p":
                student_list.print_all()
            case "x":
                FileManager.save_to_csv(filename, student_list)
                print("Data saved. Exiting...")
                break
            case _:
                print("Invalid option.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
    else:
        main(sys.argv[1])
