# Ініціалізуємо словники
numbers = {1: "One", 2: "Two", 3: "Three"}
numbersTest = {4: "four"}

# Виводимо початковий словник в консоль
print("Initial numbers dictionary:", numbers)

# Оновлюємо словник, додаючи елементи з numbersTest
numbers.update(numbersTest)
print("Updated numbers dictionary:", numbers)

# Видаляємо елемент з ключем 2
if 2 in numbers:
    del numbers[2]
    print("Dictionary after deleting key 2:", numbers)
else:
    print("Key 2 not found in the dictionary.")

# Виводимо ключі словника
print("Keys in the dictionary:", numbers.keys())

# Виводимо значення словника
print("Values in the dictionary:", numbers.values())

# Виводимо всі пари ключ-значення словника
print("Items in the dictionary:", numbers.items())

# Очищаємо словник
numbers.clear()
print("Dictionary after clearing all items:", numbers)
