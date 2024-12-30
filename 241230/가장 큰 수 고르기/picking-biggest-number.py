arr = list(map(int, input().split()))

num = arr[0]

for elem in arr[1:]:
    if elem > num:
        num = elem

print(num)