import requests

# Функція для отримання курсу валюти з API НБУ
def get_exchange_rate(currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['rate']  # Повертаємо курс валюти
    return None

# Функція для запиту скільки гривень конвертувати
def user_input_uah():
    uah = input("Введіть кількість гривень для конвертації: ")
    try:
        uah_amount = float(uah) # переводимо в float
        if uah_amount < 0: # не може бути -1
            print("Сума не може бути від'ємною. Спробуйте ще раз.")
        else:
            return uah_amount  # Повертаємо значення як додатне число
    except ValueError: 
        print("Введено некоректне значення. Спробуйте ще раз.")
        return user_input_uah() # повертаємо функцію

# Функція для запиту валюти у користувача
def user_input_convert():
    user_currency = input("Введіть валюту, в яку треба конвертувати (USD, EUR, PLN): ").upper()
    if user_currency in ["USD", "EUR", "PLN"]:
        return user_currency  # Повертаємо введену валюту
    else:
        print("Невірний код валюти. Спробуйте ще раз.")
        return user_input_convert()

# Функція для конвертації гривень у вибрану валюту
def convert_uah_to_currency(uah_amount, exchange_rate):
    return uah_amount / exchange_rate if exchange_rate else None

def main():
    while True:
        user_uah = user_input_uah()  # Отримуємо кількість гривень
        user_currency = user_input_convert()  # Отримуємо валюту від користувача
        exchange_rate = get_exchange_rate(user_currency)  # Отримуємо курс валюти
        
        if exchange_rate:
            converted_amount = convert_uah_to_currency(user_uah, exchange_rate)
            print(f"Курс {user_currency} до гривні: {exchange_rate}")
            print(f"{user_uah} гривень = {converted_amount:.2f} {user_currency}")
        else:
            print("Не вдалося отримати курс валюти. Спробуйте пізніше.")
        break

main()
