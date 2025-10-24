initial_number = int(input("Enter 4-digit number "))

first_num, fourth_num = divmod(initial_number, 10)
first_num, third_num = divmod(first_num, 10)
first_num, second_num = divmod(first_num, 10)

print(first_num, second_num, third_num, fourth_num, sep="\n")
