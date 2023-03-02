def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            try:
                for n in range(len(sub_string)):
                    if string[i + n] != sub_string[n]:
                        break
                else:
                    count += 1
            except IndexError:
                break
    return count

print(count_substring("ABCDCDC", "CDC"))
