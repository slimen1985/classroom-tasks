def split_by_symbol(text: str, separator: str) -> list:
    result = []
    words = []
    for char in text:
        if char != separator:
            words.append(char)
        else:
            result.append("".join(words))
            words.clear()
    result.append("".join(words))
    return result

text = input('Enter any text: ')
print(split_by_symbol(text, " "))