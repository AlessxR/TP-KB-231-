def inputList(my_list):
    my_list = ["privet", "kak", "dela?"]
    print(my_list)  # Вивід списку в консоль

def extendList(my_list):
    my_list.extend(["hi"])  # Розширюємо список, додаючи "hi" як один елемент
    print(my_list)

def appendList(my_list):
    my_list.append("normalno a tvoi?")  # Додаємо "normalno a tvoi?" в кінець списку
    print(my_list)

def insertList(my_list):
    my_list.insert(0, "ya tut")  # Додаємо "ya tut" на початок списку, по індексу 0
    print(my_list)

def removeList(my_list):
    if "ya tut" in my_list:
        my_list.remove("ya tut")  # Видаляємо "ya tut" зі списку
    print(my_list)

def sortList(my_list):
    my_list.sort()  # Сортування списку
    print(my_list)

def reverseList(my_list):
    my_list.reverse()  # Реверс списку
    print(my_list)

def copyList(my_list):
    copied_list = my_list.copy()  # Копіювання списку
    print(copied_list)
    return copied_list

def clearList(my_list):
    my_list.clear()  # Очищення всіх елементів списку
    print(my_list)

# Приклад
my_list = []
inputList(my_list)  # Створюємо початковий список
extendList(my_list)  # Розширюємо список
appendList(my_list)  # Додаємо елемент в кінець списку
insertList(my_list)  # Вставляємо елемент на початок списку
removeList(my_list)  # Видаляємо певний елемент зі списку
sortList(my_list)  # Сортуємо список
reverseList(my_list)  # Робимо реверс списку
copyList(my_list)  # Копіюємо список
clearList(my_list)  # Очищаємо список
