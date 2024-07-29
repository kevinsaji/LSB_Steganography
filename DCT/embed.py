import numpy as np
#enter the data to the blocks excluding the DC val and those with 0 and 1s in the dct

def embed(bin_text, blocks):
    index = 0
    for block in blocks:
        for i in range(8):
            for j in range(8):
                if index == len(bin_text):   #finished embed
                        return -1
                if i == 0 and j == 0:   #skip the DC val
                    continue
                if block[i][j] <= 1:  #skip 0s and 1s
                    continue
                if int(bin_text[index]) == (block[i][j] % 2):  #both the LSB and required bit are the same
                    index += 1
                    continue
                if block[i][j] % 2 == 0:
                    block[i][j] += 1
                else:
                    block[i][j] -= 1
                index += 1
    return index
                    
