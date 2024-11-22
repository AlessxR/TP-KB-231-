stud = [
    {"name": "Pimpam", "score": "10"},
    {"name": "Airmpor", "score": "11"},
    {"name": "Eirmor", "score": "7"}
]

while True:
    sort_by = input("Введіть параметр для сортування(name/score): ").lower()
    
    if sort_by in ["name", "score"]:
        break  # Якщо правильний параметр, закінчуємо перевірку.
    else:
        print("Невірний параметр. Введіть заново: ")

# Сортування по параметру користувача
sorted_list = sorted(stud, key=lambda x: x["name"] if sort_by == "name" else int(x["score"]))

# Вивід отсортованного
for student in sorted_list:
    print(student)
