arr = list(map(int, input().split()))
cnt_arr = [0]*10

for num in arr:
    if num == 0:
        break
    else:
        cnt_arr[num//10] += 1

for i in range(1, 10):
    print(f"{i} - {cnt_arr[i]}")