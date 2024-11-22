class Example: # Приклад з __str__
    def __init__(self, name): # Конструктор класа, створення об'єкту
        self.name = name;

    def __str__(self): # Повертає читабельне представлення про об'єкт
        return f"Name: {self.name}"

example1 = Example("Oleksandr")

print(example1)


# ----------------------------------------------------- #

class Example2: # Приклад без __str__
    def __init__(self, surname):
        self.surname = surname;

example2 = Example2("Mibaror")
print(example2)
