import string

def get_incryptions(stroka:str) -> str | None:
    alphabet = string.ascii_lowercase
    n = 13
    output = str()
    for i in stroka:
        if i in alphabet:
            output += get_i(i, alphabet)
        else:
            return None
    return output

def get_i(char: str, abc: str) -> str:
    n = 13
    i_index = abc.index(char)
    new_index = (i_index + n) % len(abc)
    return abc[new_index]

some_text = input('Enter some text: ')
print(get_incryptions(some_text.lower()))
