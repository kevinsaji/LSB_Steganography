import numpy as np


'''
variables used(decode function):-
flag - counts the elements of the extracted string of hidden bits, bitwise.
num - collects all the hidden bits
out - easy brake from loop
checker - to use the 1st bytes to know how many more bits to take for efficiency
string_output - output having the data as plain text
lower - used as a way to slice the num string


Method used:-
num = num[8:] - used so that num will only have the hidden bits ... not the length of the hidden bits
for k in range(8, len(num)+8, 8): - done to slice through num(string of bits)
'''


def decode(array):
    flag = 0
    num = ''
    out = 0
    checker = None
    for i in range(np.shape(array)[0]):
        for j in range(np.shape(array)[1]):
            for k in [7, 15, 23]:
                num += str(array[i, j, k])
                flag += 1
                if flag == checker:
                    out = 1
                    break
                if flag == 16:
                    checker = 16 + (int(num, 2) * 8)
                    print(int(num, 2))
            if out == 1:
                break
        if out == 1:
            break
    num = num[16:]
    string_output = ''
    lower = 0
    for k in range(8, len(num) + 8, 8):
        string_output += chr(int(str(num[lower:k]), 2))
        lower = k
    return string_output


