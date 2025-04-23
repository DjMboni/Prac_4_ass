# Initial list of numbers
numbers = [3, 5, 7, 9, 8, 0]
print("Original list:", numbers)

# Display the menu of operations
print("Select an operation (+, -, *, /):")
operation = input()

if operation in ['+', '-', '*', '/']:
    # Get a number between 1 and 9 from the user
    num_str = input("Enter a number between 1 and 9: ")
    operand = float(num_str)
    while not (1 <= operand <= 9):
        print("Number must be between 1 and 9. Please try again.")
        num_str = input("Enter a number between 1 and 9: ")
        operand = float(num_str)

    # Create a new list to store the calculated results
    results = []

    # Loop through the original list and perform the chosen operation
    for number in numbers:
        if operation == '+':
            results.append(number + operand)
        elif operation == '-':
            results.append(number - operand)
        elif operation == '*':
            results.append(number * operand)
        elif operation == '/':
            if operand == 0:
                results.append("Division by zero!")
            else:
                results.append(number / operand)

    # Display the old list and the newly generated list
    print("Original list:", numbers)
    print("New list with results:", results)

else:
    print("Invalid operation selected.")




