n = int(input())
sum = 0
cnt = 0
for i in range(n):
    s = input()
    sum += len(s)
    if s[0]=='a':
        cnt += 1

print(sum, cnt)