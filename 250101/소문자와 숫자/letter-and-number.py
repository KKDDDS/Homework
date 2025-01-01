a = list(input())

for elem in a:
    if elem.isalpha():
        print(elem.lower(), end='')
    elif elem.isdigit():
        print(elem, end='')