a, b = map(str, input().split())

x = a.find(b)

if x == -1:
    print("No")
else:
    print(x)