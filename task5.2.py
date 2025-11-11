"""
Модифікувати калькулятор таким чином, щоб він працював доти,
доки користувач цього хоче. Тобто, потрібно робити запит до користувача на продовження
роботи калькулятора після кожного обчислення - якщо користувач ввів yes (можна просто y),
то нове обчислення, інакше - закінчення роботи.
"""

while True:
    number1 = float(input("Enter first number "))
    number2 = float(input("Enter second number "))
    math_operation = input("Enter arithmetic operation ")

    if math_operation == "+":
        print(number1 + number2)
    elif math_operation == "-":
        print(number1 - number2)
    elif math_operation == "*":
        print(number1 * number2)
    elif math_operation == "/":
        print(number1 / number2 if number2 else print("Division by 0 is not allowed"))
    else:
        print("You entered unacceptable arithmetic operation")

    if input("Enter 'y' or 'yes' if you want to continue ").lower() not in ("yes", "y"):
        break