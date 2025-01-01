a = input()
print(a)
for i in range(len(a)):
    a = a[-1]+a[:-1]
    print(a)