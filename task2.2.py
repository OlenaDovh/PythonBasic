initial_number = int(input("Enter 5-digit number "))

initial_number, fifth_num = divmod(initial_number, 10)
fifth_num *= 10000
initial_number, fourth_num = divmod(initial_number, 10)
fourth_num *= 1000
initial_number, third_num = divmod(initial_number, 10)
third_num *= 100
initial_number, second_num = divmod(initial_number, 10)
second_num *= 10
initial_number, first_num = divmod(initial_number, 10)

reversed_num = first_num + second_num + third_num + fourth_num + fifth_num

print("Reversed number is", reversed_num)
