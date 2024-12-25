a, b = map(int, input().split())


while a>=b:
    print(a, end=' ')
    a -= 1

if b>a:
    while b>=a:
        print(b, end=' ')
        b -= 1