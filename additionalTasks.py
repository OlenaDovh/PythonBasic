# TASK_1
# def reverse_words(sentence):
#     new_sentence = sentence.split(" ")
#     final_sentence = []
#     for i in new_sentence:
#         final_sentence.append(str(i[::-1]))
#     str_sentence_value = " ".join([str(i) for i in final_sentence])
#     return str_sentence_value
#
# assert reverse_words("Hello world") == 'olleH dlrow', 'Test1'
# assert reverse_words("Python is fun") == 'nohtyP si nuf', 'Test2'
# assert reverse_words("Quick brown fox") == 'kciuQ nworb xof', 'Test3'
# assert reverse_words("Just a test") == 'tsuJ a tset', 'Test4'
# assert reverse_words("123 456") == '321 654', 'Test5'
# print("OK")
# from math import sqrt


#TASK_2
# import math
#
# def calculate_circle_area(radius):
#     area = (radius**2 * math.pi)
#     return round(area, 2)
#
# print(calculate_circle_area(10))

# TASK_3
# def find_gcd(a, b):
#     max_num = max(a, b)
#     min_num = min(a, b)
#     remainder = 1
#     while min_num > 0:
#         remainder = max_num % min_num
#         max_num, min_num = min_num, remainder
#     return max_num
#
# find_gcd(1071, 462)

#TASK4
# def sum_of_digits(number):
#     number = str(number)
#     sign = ""
#     summa = 0
#     for i in number:
#         if i.isalnum():
#             summa += int(i)
#     return summa
#
# sum_of_digits(-456)

#TASK5
# def get_option(lst):
#     max_gold = 0
#     options = []
#     if len(lst) -1 == None:
#         return max_gold
#     else:

# TASK6
# def calculator(num1, num2, operation):
#     if operation == "+":
#         result = num1 + num2
#     elif operation == "-":
#         result = num1 - num2
#     elif operation == "*":
#         result = num1 * num2
#     elif operation == "/":
#         result = num1 / num2 if num2 else 0
#     else:
#         result = 0
#
#     return result

#TASK7
# def multiply_even_numbers(numbers):
#     """
#     Помножує всі парні числа у списку на 2.
#
#     :param numbers: Список чисел.
#     :return: Новий список з парними числами, помноженими на 2.
#     """
#     result = []
#     for i in numbers:
#         print(i, numbers, result)
#         if i % 2 == 0:
#             result.append(i * 2)
#     return result
#
# # Перевірка
# assert multiply_even_numbers([1, 2, 3, 4, 5, 6]) == [4, 8, 12]

#TASK10.2

# def is_even(digit):
#     if digit == 0:
#         return True
#     if digit == 1:
#         return False
#     else:
#         return is_even(digit - 2)


# import timeit
#
# def measure(value):
#     return timeit.timeit(lambda: is_even(value), number=1_000_000)
#
# print(measure(10))
# print(measure(123456789))
# print(measure(2**1000))

#Створіть функцію, яка приймає список чисел і повертає новий список, де кожне число замінено його квадратом.

# def square_numbers(numbers):
#     """
#     Замінює кожне число у списку його квадратом.
#
#     :param numbers: Список чисел.
#     :return: Новий список з квадратами чисел.
#     """
#     result = []
#     if not numbers:
#         return result
#
#     result = [numbers[0] ** 2] + square_numbers(numbers[1:])
#     return result
#
# # Перевірка
# assert square_numbers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
# assert square_numbers([0, -1, -2, -3]) == [0, 1, 4, 9]
# assert square_numbers([]) == []
# print("OK")

#Напишіть рекурсивну функцію для обчислення факторіалу числа.

# def factorial(num):
#     """
#     Обчислює факторіал числа num.
#
#     :param n: Ціле число.
#     :return: Факторіал числа num.
#     """
#
#     if num == 0:
#         return 1
#
#     return num * factorial(num - 1)
#
# # Перевірка
# assert factorial(5) == 120



# TASK
# def prime_generator(end):
#     for num in range(2, end + 1):
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield num
#
#
# print(list(prime_generator(10)))
# print(list(prime_generator(15)))
# print(list(prime_generator(29)))