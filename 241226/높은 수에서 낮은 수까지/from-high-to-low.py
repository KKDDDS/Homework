a, b = map(int, input().split())
n= a

while n>=b:
    print(n, end=' ')
    n -= 1

if b>a:
    while b>=a:
        print(b, end=' ')
        b -= 1