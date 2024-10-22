from bisect import bisect_left

def search_position(lst, element):
    """Знаходить позицію для вставки елементу у відсортований список."""
    return bisect_left(lst, element)

def main():
    my_list = ["one", "two", "three", "four"]
    my_list.sort()  # Сортуємо початковий список

    print("Початковий відсортований список:", my_list)

    while True:
        user_input = input("Введіть елемент для вставки в масив або 'exit' для виходу: ")
        if user_input.lower() == "exit":
            print("Вихід з програми.")
            break

        position = search_position(my_list, user_input)
        print(f"Позиція для вставки '{user_input}': {position}")

        my_list.insert(position, user_input)
        print("Оновлений список:", my_list)

main()
