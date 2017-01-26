def alphabet_position(letter):
    letter_list = ("abcdefghijklmnopqrstuvwxyz")
    if type(letter) == str and letter.isalpha():
        return letter_list.index(letter.lower())
    return letter_list[letter]


def rotate_character(char, rot):
    upper_case = False
    if char.isalpha():
        if char.isupper():
            upper_case = True
        new_num = (alphabet_position(char)+ rot) %26
        new_letter = alphabet_position(new_num)
        if upper_case == True:
            return new_letter.upper()
        return new_letter
    return char

def encrypt(text, rot):
    new_text = []
    for i in text:
        new_text.append(rotate_character(i, rot))
    new_text = "".join(new_text)
    return new_text
