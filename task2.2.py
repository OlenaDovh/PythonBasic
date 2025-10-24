initial_number = int(input("Enter 5-digit number "))

first_num, fifth_num = divmod(initial_number, 10)
first_num, fourth_num = divmod(first_num, 10)
first_num, third_num = divmod(first_num, 10)
first_num, second_num = divmod(first_num, 10)

print(fifth_num, fourth_num, third_num, second_num, first_num, sep="")
