n = int(input())
for i in range(1, n+1):
    if i %2 ==1:
        a = i//2 + 1
        for k in range(a):
            print("*", end=' ')
    else:
        b = n-(i-(i//2)-1)
        for l in range(b):
            print("*", end=' ')
    print()

for j in range(n, 0, -1):
    if j%2==1:
        c = j//2 + 1
        for z in range(c):
            print("*", end=' ')
    else:
        d = n-(j-(j//2)-1)
        for y in range(d):
            print("*", end=' ')
    print()
