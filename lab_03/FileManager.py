import csv
from Student import Student
from StudentList import StudentList

class FileManager:
    @staticmethod
    def load_from_csv(filename: str) -> StudentList:
        student_list = StudentList()
        try:
            with open(filename, newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    student = Student(row["name"], row["phone"], row["surname"], row["course"])
                    student_list.add_student(student)
        except FileNotFoundError:
            print(f"File {filename} not found.")
        return student_list

    @staticmethod
    def save_to_csv(filename: str, student_list: StudentList):
        try:
            with open(filename, mode="w", newline='', encoding="utf-8") as csvfile:
                fieldnames = ["name", "phone", "surname", "course"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for student in student_list.to_dict_list():
                    writer.writerow(student)
        except IOError:
            print(f"Error writing to file {filename}.")
