n = int(input())
cnt = 0
print(n, end=' ')
nn = n
while cnt != 2:
    nn += n
    print(nn, end=' ')
    if nn%5 ==0:
        cnt += 1