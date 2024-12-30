n = int(input())

arr = list(map(int, input().split()))

min_num = 100
for i in range(n):
    for j in range(n):
        if 0< arr[j] - arr[i] <min_num:
            min_num = arr[j] - arr[i]

print(min_num)
