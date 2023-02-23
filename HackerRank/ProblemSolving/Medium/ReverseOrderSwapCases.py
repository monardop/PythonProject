def reverse_words_order_and_swap_cases(sentence: str):
    new_str = ""
    for n in sentence:
        if n.isupper():
            new_str += n.lower()
        else:
            new_str += n.upper()
    string_splited = new_str.split()
    final_string = ""
    for n in range(-1, - (len(string_splited)+1), -1):
        final_string += string_splited[n] + " "
    return final_string.strip()
reverse_words_order_and_swap_cases("Pablo Es GeNio")
