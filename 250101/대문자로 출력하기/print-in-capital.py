a = list(map(str, input().split(".")))

for elem in a:
    if elem.isalpha():
        print(elem.upper(), end='')