a, b = map(int, input().split())
print(f"{a//b}.", end='')
m = a%b
for i in range(20):
    n = m*10//b
    m = m*10%b
    print(n,end='')
