"""
Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв

Приклад:
"a-c" -> abc
"a-a" -> a
"s-H" -> stuvwxyzABCDEFGH
"a-A" -> abcdefghijklmnopqrstuvwxyzA
"""
import string

# input_set = "a-c" #-> abc
# input_set = "a-a" #-> a
# input_set = "s-H" #-> stuvwxyzABCDEFGH
input_set = "a-A" #-> abcdefghijklmnopqrstuvwxyzA

start_index = string.ascii_letters.find(input_set[0])
end_index = string.ascii_letters.find(input_set[-1])

result = string.ascii_letters[start_index:end_index + 1]

print(result)
