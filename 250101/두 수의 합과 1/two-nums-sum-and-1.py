a, b = map(int, input().split())

c = list(str(a+b))
cnt = 0

for elem in c:
    if elem == '1':
        cnt += 1

print(cnt)