n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = False
for i in range(n1-n2+1):
    n = 0
    while A[i] == B[n]:
        i += 1
        n += 1
        if A[i] == B[-1]:
            ans = True
            break

if ans==True:
    print("Yes")
else:
    print("No")
