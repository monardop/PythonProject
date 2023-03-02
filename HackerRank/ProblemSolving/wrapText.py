def wrap(string: str, max_width: int):
    new_text = ""
    for i, letter in enumerate(string):
        if i != 0 and i % max_width == 0:
            new_text += "\n"
        new_text += letter
    return new_text


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
