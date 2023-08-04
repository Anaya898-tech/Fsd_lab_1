def find_max(lst):
    if not lst:
        return None

    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element

    return max_element

# Take user input for the list of numbers
try:
    input_list = [int(num) for num in input("Enter a list of numbers separated by spaces: ").split()]
    print("List:", input_list)
    print("Max element:", find_max(input_list))
except ValueError:
    print("Invalid input! Please enter a list of numbers separated by spaces.")
