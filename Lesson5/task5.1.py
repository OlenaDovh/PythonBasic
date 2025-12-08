"""
Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.

Змінна не може:
починатися з цифри
містити великі літери,
пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
бути жодним із зареєстрованих слів.
При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".

Список зареєстрованих слів можна взяти із keyword.kwlist.

У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.

_ => True
__ => False
___ => False
x => True
get_value => True
get value => False
get!value => False
some_super_puper_value => True
Get_value => False
get_Value => False
getValue => False
3m => False
m3 => True
assert => False
assert_exception => True
"""
import keyword
import string

input_var = "" # => False
# input_var = "_" # => True
# input_var = "__" # => False
# input_var = "___" # => False
# input_var = "x" # => True
# input_var = "get_value" # => True
# input_var = "get value" # => False
# input_var = "get!value" # => False
# input_var = "some_super_puper_value" # => True
# input_var = "Get_value" # => False
# input_var = "get_Value" # => False
# input_var = "getValue" # => False
# input_var = "3m" # => False
# input_var = "m3" # => True
# input_var = "assert" # => False
# input_var = "assert_exception" # => True

approval_for_var = False

# рядок не пустий
if input_var:
    # рядок не є зарезервованим словом
    if  not keyword.iskeyword(input_var):
        # рядок не має спец. симоволів і пробіл
        if all (char not in string.punctuation.replace("_", " ") for char in input_var):
            # рядок не має великих літер
            if not (char.isupper() for char in input_var):
                # рядок не починається з цифри
                if not input_var[0].isdigit():
                    # рядок не має більше 1 нижнього підкреслення підряд
                    if not "__" in input_var:
                        # тоді рядок можна вважати правильною назвою змінної
                        approval_for_var = True

print("Variable name is", approval_for_var)