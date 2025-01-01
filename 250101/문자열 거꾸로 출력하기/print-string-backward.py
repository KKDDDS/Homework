a = True

while a:
    string = input()
    if string == 'END':
        a = False
    else:
        print(string[::-1])