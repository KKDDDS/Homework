arr = list(map(int, input().split()))
sum = 0
cnt = 0
for num in arr:
    if num < 250:
        sum += num
        cnt += 1
    else:
        break

print(f"{sum} {(sum/cnt):.1f}")
