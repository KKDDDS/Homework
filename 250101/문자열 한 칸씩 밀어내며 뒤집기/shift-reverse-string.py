a, q = input().split()
q = int(q)

for i in range(q):
    rqst = int(input())

    if rqst == 1:
        a = a[1:]+a[0]
        print(a)

    elif rqst == 2:
        a = a[-1]+a[:-1]
        print(a)

    elif rqst == 3:
        a = a[::-1]
        print(a)
