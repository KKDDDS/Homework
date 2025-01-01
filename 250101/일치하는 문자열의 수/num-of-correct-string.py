n, A = map(str, input().split())
cnt = 0
for i in range(int(n)):
    string = input()
    if string == A:
        cnt += 1

print(cnt)