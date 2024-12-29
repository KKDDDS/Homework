arr = list(map(int, input().split()))
cnt_arr = [0]*11

for num in arr:
    if num == 0:
        break
    else:
        cnt_arr[num//10] += 1

for i in range(10, 0, -1):
    print(f"{i*10} - {cnt_arr[i]}")