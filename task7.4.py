"""
Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range) для 100 елементів,
за наступними правилом:
Один список з числами кратними 3, інший з кратними числами 5.
За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
Функція повинна повернути цю множину як результат своєї роботи.

def common_elements():
		pass

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
"""

def get_list_of_multiplication(num):
    multiples= []
    for i in range(100):
        if i % num == 0:
            multiples.append(i)
    return multiples

def common_elements():
    multiples_of_3 = set(get_list_of_multiplication(3))
    multiples_of_5 = set(get_list_of_multiplication(5))
    multiples_of_3_and_5 = multiples_of_5.intersection(multiples_of_3)
    return multiples_of_3_and_5

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')