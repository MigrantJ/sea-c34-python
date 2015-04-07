import string

# create a string containing all lowercase letters
l_alpha = "".join([chr(i) for i in range(97, 123)])
# create the translation string, all chars offset by 13
l_alpha_offset = l_alpha[13:] + l_alpha[:13]
# include uppercase
l_alpha += l_alpha.upper()
l_alpha_offset += l_alpha_offset.upper()


def rot13(input_string):
    # todo: input validation
    table = string.maketrans(l_alpha, l_alpha_offset)
    translated_string = input_string.translate(table)

    return translated_string


if __name__ == "__main__":
    print(rot13("Uryc, V'z n sernx."))