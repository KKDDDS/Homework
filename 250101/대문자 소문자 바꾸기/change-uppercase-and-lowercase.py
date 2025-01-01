a = list(input())

for elem in a:
    if 'A' <= elem <= 'Z':
        print(elem.lower(), end='')
    else:
        print(elem.upper(),end='')