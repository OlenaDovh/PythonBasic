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



#TASK_2
# import math
#
# def calculate_circle_area(radius):
#     area = (radius**2 * math.pi)
#     return round(area, 2)
#
# print(calculate_circle_area(10))

# TASK_3
def find_gcd(a, b):
    gcd = 0
    dil = 1
    while dil > 0:
        dil = divmod(a, b)
        dil = divmod(b,dil)
    print(dil)


    print(divmod(a, 10))
    print(divmod(b, 10))

find_gcd(7, 11)