initial_number = int(input("Enter 4-digit number "))

first_digit, fourth_digit = divmod(initial_number, 10)
first_digit, third_digit = divmod(first_digit, 10)
first_digit, second_digit = divmod(first_digit, 10)

print("Your number in a column:", first_digit, second_digit, third_digit, fourth_digit, sep="\n")
