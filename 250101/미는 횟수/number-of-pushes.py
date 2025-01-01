A = input()
B = input()

ans = True
cnt = 0

while ans:
    if A ==B:
        ans = False
    else:
        A = A[-1]+A[:-1]
        cnt += 1

print(cnt)