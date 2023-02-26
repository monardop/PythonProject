
n = int(input())
dictionary = {}
for _ in range(n):
    new_entry = input()
    name, tel = new_entry.split()
    dictionary[name] = int(tel)

for _ in range(n):
    try:
        lookup:str = input()
        print(lookup,"=",dictionary[lookup])
    except KeyError:
        print("Not found")