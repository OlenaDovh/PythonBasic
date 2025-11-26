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