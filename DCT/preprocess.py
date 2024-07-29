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

def image_to_block(image):
    out = []
    for y in np.vsplit(image, int(image.shape[0]/8)):
        for x in np.hsplit(y, int(image.shape[1]/8)):
            out.append(x)
    return out

def block_to_dct(blocks):
    dct_blocks = [cv.dct(np.float32(block)) for block in blocks]
    return dct_blocks

def divide_by_quant(dct_blocks):
    dct_quant_blocks = [np.round(np.divide(block, jpeg_quant_table)) for block in dct_blocks]
    return np.int64(dct_quant_blocks)
