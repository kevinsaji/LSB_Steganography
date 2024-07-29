import cv2 as cv
import numpy as np

jpeg_quant_table = np.asarray([
                                [16, 11, 10, 16,  24, 40,   51,  61],
                                [12, 12, 14, 19,  26, 58,   60,  55],
                                [14, 13, 16, 24,  40, 57,   69,  56],
                                [14, 17, 22, 29,  51, 87,   80,  62],
                                [18, 22, 37, 56,  68, 109, 103,  77],
                                [24, 36, 55, 64,  81, 104, 113,  92],
                                [49, 64, 78, 87, 103, 121, 120, 101],
                                [72, 92, 95, 98, 112, 100, 103,  99]
                            ],
                            dtype = np.float32)

def multiply_by_quant(dct_quant_blocks):
    dct_quant_blocks = [np.multiply(block, jpeg_quant_table) for block in dct_quant_blocks]
    return dct_quant_blocks

def encrypted_to_blocks(encrypted_blocks):
    blocks = [cv.idct(np.float32(block)) for block in encrypted_blocks]
    return blocks

def blocks_to_image(blocks, pixel_count):
    image = []
    temp = []
    blocks_per_row = pixel_count//8
    for i in range(len(blocks)):
        if i > 0 and not(i % blocks_per_row):
            image.append(temp)
            temp = [blocks[i]]
        else:
            temp.append(blocks[i])
    if i % blocks_per_row != 0:
        image.append(temp)
    return np.block(image)