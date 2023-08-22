import numpy as np
import cv2
import os
from text_to_bin import text_to_bin
from decode import decode
import gui

'''
variables used:-
text_to_bin(user_input) - this give the binary output for the user inputted text
im - this is the numpy array that had the pixel values as decimal
bin_array - this is the numpy array that had the pixel values as binary digits
new_array - final output array having values as binary


encode function:-
flag - this was used to iterate over all the elements of the bin_string
checker - this was used as a measure to stop indexing error for bin_string and break the whole loop


Method for encode function:-
'i' was used to iterate over all the rows while 'j' was used to iterate over all the columns, i took the 7,15,23 rd 
element because it technically is the 8th, 16th and 24th element and array[i,j] will give a list of all rgb values in 
one list itself.

'''


def encode(array, bin_string):
    flag = 0
    checker = 0
    for i in range(np.shape(array)[0]):
        for j in range(np.shape(array)[1]):
            for k in [7, 15, 23]:
                array[i, j, k] = int(bin_string[flag])
                flag += 1
                if flag == len(bin_string):
                    checker = 1
                    break
            if checker == 1:
                break
        if checker == 1:
            break
    return array


if gui.e_d_func() == 1:

    im = cv2.imread(r"{filename}".format(filename=gui.root.filename))
    norm_image = im

    bin_array = np.unpackbits(im, axis=2)
    max_char = ((np.shape(bin_array)[1] * 3) * (np.shape(bin_array)[0])) / 8

    user_input = gui.text_func()

    new_array = encode(bin_array, text_to_bin(user_input))

    final_array = np.packbits(new_array, axis=2)

    os.chdir(r'C:\Users\kevin\Desktop')  # give the location to store the final formatted image here

    cv2.imwrite('stego_image.png', final_array)

# ------decode------
else:
    check1 = cv2.imread(r"{filename}".format(filename=gui.root.filename))
    check2 = np.unpackbits(check1, axis=2)
    print(decode(check2))
