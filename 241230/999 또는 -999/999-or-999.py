arr = list(map(int, input().split()))

max_num = arr[0]
min_num = arr[0]

for elem in arr:
    if elem == 999 or elem == -999:
        break
    if max_num<elem:
        max_num = elem
    elif min_num > elem:
        min_num = elem

print(max_num, min_num, sep=' ')