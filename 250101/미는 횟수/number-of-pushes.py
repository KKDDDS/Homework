A = input()
B = input()

cnt = 0

for i in range(len(A)):
    if A ==B:
        print(cnt)
        break
    else:
        A = A[-1]+A[:-1]
        cnt += 1
if A != B:
    print(-1)