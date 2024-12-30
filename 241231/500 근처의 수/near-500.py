arr = list(map(int, input().split()))

max_num = 1
min_num = 1000

for elem in arr:
    if max_num<elem<500:
        max_num = elem
    elif 500<elem<min_num:
        min_num = elem

print(max_num, min_num)