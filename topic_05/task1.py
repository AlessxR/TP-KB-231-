import random # імпорт модуля

rules = {
    "stone" : "scissor", # "stone" - ключ, "scissor" - значення
    "scissor" : "paper",
    "paper" : "stone"
} # вибір: що перемагає

def choice():
    choice = input("Введіть вибір (stone, scissor, paper) або 'exit' для виходу: ").strip().lower() # Запитуємо
    while choice not in rules and choice != "exit": # Перевірка введеного
        print("Неправильний вибір. Спробуйте ще раз.")
        choice = input("Введіть вибір (stone, scissor, paper) або 'exit' для виходу: ").strip().lower()
    return choice # Повертання вибору


def get_computer_choice():
    # Вибір з ключів rules
    return random.choice(list(rules.keys()))

def winner(user_choice, comp_choice): # Порівняння користувача та комп'ютера
    if user_choice == comp_choice:
        return "Нічия"
    elif rules[user_choice] == comp_choice:
        return "Ви виграли!"
    else:
        return "Комп'ютер виграв"
    
def play():
    while True:
        user = choice() # Вибір користувача

        if user == "exit".lower():
            break

        computer = get_computer_choice()
        print(f"Вибір комп'ютера: {computer}")

        result = winner(user, computer)
        print(f"Результат гри: {result}")

play()