N = int(input())
arr = list(map(int, input().split()))

minnum = arr[0]
for num in arr[1:]:
    if minnum>num:
        minnum = num

cnt = 0

for elem in arr:
    if elem == minnum:
        cnt +=1

print(minnum, cnt, sep=' ')