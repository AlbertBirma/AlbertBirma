"""
A program , which makes statistics of words in input string. On the left side of output : the quantity of letters in one word .
On the right side : the quantity of words with specific quantity of letters.
"""
# Basic code realization with one function

import collections as colt

list_num = []

def Counter():
    str_input = input('Введите предложение: ').split()
    for element in str_input:
        list_num.append(len(element))
    count_dict = dict(colt.Counter(list_num))
    sorted_dict = dict(sorted(count_dict.items()))
    for key, value in sorted_dict.items():
        print(f'{key}: {value}')
Counter()
