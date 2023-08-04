# Take user input for the list of numbers
try:
    input_list = [int(num) for num in input("Enter a list of numbers separated by spaces: ").split()]
    print("List:", input_list)
    min_element = min(input_list)
    max_element = max(input_list)
    print("Min element:", min_element)
    print("Max element:", max_element)
except ValueError:
    print("Invalid input! Please enter a list of numbers separated by spaces.")
