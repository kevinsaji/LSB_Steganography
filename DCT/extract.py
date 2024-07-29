import numpy as np
#extract data from the image

def extract(blocks):
    binArr = []
    flag = 0 #showing if the text is complete 0 is false 1 is true
    for block in blocks:
        for i in range(8):
            for j in range(8):
                if i == 0 and j == 0 :   #skip the DC val
                    continue
                if block[i][j] <= 1 :  #skip 0s and 1s
                    continue
                binArr.append(str(block[i][j]%2))
    binTxt = ''.join(binArr)
    #byte_chunks = [binTxt[i:i+8] for i in range(0, len(binTxt), 8)]
    byte_chunks = []
    for i in range(0, len(binTxt), 8):
        if(binTxt[i:i+8] == "00000100"):   #using the ascii end of transmission value
            flag = 1
            break
        byte_chunks.append(binTxt[i:i+8])
        
    text = ''.join([chr(int(byte, 2)) for byte in byte_chunks if len(byte) == 8])
    return text, flag