def text_to_bin(user_input):
    out_string = f'{len(user_input):016b}'
    for i in user_input:
        out_string += str(format(ord(i), '08b'))
    return out_string


