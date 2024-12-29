n = int(input())
arr=[1]
arr.append(n)
nn = 0
while arr[-1]<100:
    nn = arr[-1]+arr[-2]
    arr.append(nn)

for num in arr:
    print(num, end=' ')