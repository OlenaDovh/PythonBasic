"""
Ваша функція is_even повинна повертати True якщо число парне, і False якщо число непарне.
Вхідні дані: Ціле число.
Вихідні дані: Логічний тип.
"""

def is_even(digit):
    if digit < 0:
        return is_even(-digit)
    if digit == 0:
        return True
    if digit == 1:
        return False
    else:
        return is_even(digit - 2)

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
assert is_even(-2) == True, 'Test4'
assert is_even(-5) == False, 'Test5'
print('OK')