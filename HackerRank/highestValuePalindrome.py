def isPalindrome(string):
    string = "".join(string)
    reversed_str = string[::-1]
    count = 0
    for a,b in zip(string, reversed_str):
        if a != b:
            count += 1
    return count

def highestValuePalindrome(s: str, n: int, k: int):
    # Write your code here

    if n == 1 and k == 1:
        return "9"

    new_string = [n for n in s]
    i = 0
    
    while k != 0 and i <= (n // 2) - 1:
        a = 0 + i
        b = -1 - i
        if new_string[a] != new_string[b]:
            if k >= 2:
                new_string[a] = "9"
                new_string[b] = "9"
                k -= 2
            else: 
                if int(new_string[a]) < int(new_string[b]):
                    new_string[a] = new_string[b]
                    k -= 1
                else:
                    new_string[b] = new_string[a]
                    k -= 1
        i += 1
    
    i = 0
    while k >= 2 and i <= (n // 2) - 1:
        a = 0 + i
        b = -1 - i
        if new_string[a] != "9":
            new_string[a] = "9"
            new_string[b] = "9"
            k -= 2
        i += 1

    if n % 2 != 0 and k > 0:
        new_string[n//2] = "9"

    if isPalindrome(new_string) == 0:
        return "".join(new_string)
    else: 
        return "-1"

