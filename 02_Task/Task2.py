import random


def generate_random_numbers(min_num, max_num, quantity):
    random_numbers = []

    for i in range(quantity):
        random_numbers.append(round(random.uniform(min_num, max_num), 2))
    return random_numbers


def sort_numbers_descending(numbers_list):
    sorted_list = sorted(numbers_list,  reverse=True)
    return sorted_list


def display_sorted_random_numbers():
    min_num = 0
    max_num = 0
    while True:
        try:
            min_num = float(input("Enter the minimum value for the range (minimum 3.5): "))
            if min_num < 3.5:
                print("Minimum value should be 3.5 or greater.")
                continue
            max_num = float(input("Enter the maximum value for the range (maximum 121): "))
            if max_num > 121:
                print("Maximum value should be 121 or smaller.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    quantity = 100
    random_numbers = generate_random_numbers(min_num, max_num, quantity)
    sorted_numbers = sort_numbers_descending(random_numbers)

    print("Generated random numbers:", random_numbers)
    print("Sorted random numbers (descending order):", sorted_numbers)


if __name__ == "__main__":

display_sorted_random_numbers()