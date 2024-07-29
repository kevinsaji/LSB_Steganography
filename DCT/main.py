import  cv2 as cv
import preprocess
import postprocess
import embed
import extract
import numpy as np


user_text = "Enter your text here"
bin_text = ''.join(format(ord(x), '08b') for x in user_text)
bin_text += "00000100"
#embed the data
image = cv.imread('mountains.jpg')  #put the image here
image = cv.resize(image, (image.shape[1]-image.shape[1]%8, image.shape[0]-image.shape[0]%8))
B, G, R = cv.split(image)
ycbcr_image = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
Y, Cb, Cr = cv.split(ycbcr_image)
#do Cr part first
Cr_blocks = preprocess.image_to_block(Cr)
Cr_dct_blocks = preprocess.block_to_dct(Cr_blocks)
Cr_dct_quant_blocks = preprocess.divide_by_quant(Cr_dct_blocks) 
index = embed.embed(bin_text, Cr_dct_quant_blocks)
Cr_dct_blocks = postprocess.multiply_by_quant(Cr_dct_quant_blocks)
Cr_encrypted_blocks = postprocess.encrypted_to_blocks(Cr_dct_blocks)
Cr_encrypted = np.asarray(postprocess.blocks_to_image(Cr_encrypted_blocks, Cr.shape[1]), dtype=np.uint8)
if(index > 0):
    #too big to just fit in Cr
    Cb_blocks = preprocess.image_to_block(Cb)
    Cb_dct_blocks = preprocess.block_to_dct(Cb_blocks)
    Cb_dct_quant_blocks = preprocess.divide_by_quant(Cb_dct_blocks) 
    index = embed.embed(bin_text[index:], Cb_dct_quant_blocks)  #change to cbdctblock
    if(index > 0):
        print("text too big to fit in the image")
        exit()
    Cb_dct_blocks = postprocess.multiply_by_quant(Cb_dct_quant_blocks)
    Cb_encrypted_blocks = postprocess.encrypted_to_blocks(Cb_dct_blocks)
    Cb_encrypted = np.asarray(postprocess.blocks_to_image(Cb_encrypted_blocks, Cb.shape[1]), dtype=np.uint8)
    new_img = cv.merge([Y, Cb_encrypted, Cr_encrypted])
    new_img = cv.cvtColor(new_img, cv.COLOR_YCrCb2BGR)
else:
    new_img = cv.merge([Y, Cb, Cr_encrypted])
    new_img = cv.cvtColor(new_img, cv.COLOR_YCrCb2BGR)

cv.imwrite("embeded.png", new_img)

#extracting the data
image = cv.imread('embeded.png')
B, G, R = cv.split(image)
ycbcr_image = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
Y, Cb, Cr = cv.split(ycbcr_image)
#doing the Cr part first
Cr_blocks = preprocess.image_to_block(Cr)
Cr_dct_blocks = preprocess.block_to_dct(Cr_blocks)
Cr_dct_quant_blocks = preprocess.divide_by_quant(Cr_dct_blocks) 
Cr_text, flag = extract.extract(Cr_dct_quant_blocks)
if(flag == 0): #go through Cb if text is incomplete in Cr
    Cb_blocks = preprocess.image_to_block(Cb)
    Cb_dct_blocks = preprocess.block_to_dct(Cb_blocks)
    Cb_dct_quant_blocks = preprocess.divide_by_quant(Cb_dct_blocks)
    Cb_text, flag = extract.extract(Cb_dct_quant_blocks)
    print(Cr_text+Cb_text)
else:
    print(Cr_text)