class Student:
    def __init__(self, name: str, phone: str, surname: str, course: str):
        self.name = name
        self.phone = phone
        self.surname = surname
        self.course = course

    def __str__(self):
        return f"{self.name} {self.surname}, Phone: {self.phone}, Course: {self.course}"

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "surname": self.surname,
            "course": self.course
        }
