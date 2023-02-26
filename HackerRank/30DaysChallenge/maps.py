
n = int(input())
dictionary = {}
for _ in range(n):
    new_entry = input()
    name, tel = new_entry.split()
    dictionary[name] = int(tel)

for _ in range(n):
    try:
        lookup = input()
        print(lookup,"=",dictionary[lookup])2
        
    except KeyError:
        print("Not found")