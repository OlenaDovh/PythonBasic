"""
Програма має виконувати прості математичні дії (+, -, *, /).
Користувачеві пропонується почерзі ввести числа та дію над цими числами,
а програма, виходячи з дії, обчислює та друкує результат.
Зробити перевірку на те, що при діленні дільник не дорівнює 0!
"""

number1 = float(input("Enter first number "))
number2 = float(input("Enter second number "))
math_operation = input("Enter arithmetic operation ")
result = 0

if math_operation == "+":
    result = number1 + number2
    print(result)
elif math_operation == "-":
    result = number1 - number2
    print(result)
elif math_operation == "*":
    result = number1 * number2
    print(result)
elif math_operation == "/":
    if number2:
        result = number1 / number2
        print(result)
    else:
        print("Division by 0 is not allowed")
else:
    print("You entered unacceptable arithmetic operation")