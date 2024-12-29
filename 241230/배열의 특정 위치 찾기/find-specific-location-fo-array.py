arr= list(map(int, input().split()))
sum = 0
for i in range(1,len(arr),2):
    sum += arr[i]

avg = 0
cnt = 0
for j in range(2,len(arr),3):
    avg += arr[j]
    cnt += 1



print(f"{sum} {avg/cnt:.1f}")
