n = int(input())
sum = 0
arr = list(map(float, input().split()))
for i in range(n):
    sum += arr[i]
avg = round(sum/n, 1)

print(avg)
if avg>=4.0:
    print("Perfect")
elif avg >=3.0:
    print("Good")
else:
    print("Poor")