from bisect import bisect

my_list = ["one", "two", "three", "four"]

my_list.sort()

def search_position(lst, element): # бінарний пошук 
    return bisect(lst, element)

def main():
    while True:
        print("Input elements to insert in the array or type 'exit' to quit: ")
        user_input = input()
        if user_input.lower() == "exit":
            break

        position = search_position(my_list, user_input)
        print("Позиція для вставки ", user_input, ":", position)

        my_list.insert(position, user_input)
        print("Оновленний список: ", my_list)

main()
