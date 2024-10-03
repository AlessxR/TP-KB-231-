my_list = ["privet", "kak", "dela?"]

print(my_list) # Список в консоль

my_list.extend("hi") # Розширюємо список та додаємо h i
print(my_list)


my_list.append("normalno a tvoi?") # Розширюємо список та додаємо в кінець
print(my_list)

my_list.insert(0, "ya tut") # Додаємо "ya tut" в початок списку, по індексу 0
print(my_list)

my_list.remove("ya tut") # Видаляємо "ya tut" з початку списку
print(my_list)

my_list.sort() # Сортування списку
print(my_list)

my_list.reverse() # Реверс списку
print(my_list)

my_list.copy() # Копіювання об'єктів списку
print(my_list)

my_list.clear() # Очищення всіх елементів списку
print(my_list)
