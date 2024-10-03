numbers = {1: "One", 2:"Two", 3:"Three"}
numbersTest = {4: "four"}

print(numbers) # Виводимо словник в консоль

numbers.update(numbersTest) # Якщо немає такого пар-ключа, як в другому словнику, то доповнюємо первий
print(numbers)

del numbers[2] # Видаляємо елемент під індексом 2
print(numbers)


print(numbers.keys()) # Вивід ключів словнику 

print(numbers.values()) # Вивід значень словнику

print(numbers.items()) # Повертання нового списку 

numbers.clear() # Видалення всіх елементів в списку
print(numbers)
