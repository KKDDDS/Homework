arr = [
    list(map(int, input().split()))
    for _ in range(2)
]



for i in range(2):
    sum = 0
    for j in range(4):
        sum += arr[i][j]
    print(f"{sum//4:.1f}",end=' ')

print()

for k in range(4):
    sum = 0
    for l in range(2):
        sum += arr[l][k]
    print(f"{sum//2:.1f}", end=' ')

print()
sum = 0
for x in range(2):    
    for y in range(4):
        sum += arr[x][y]
print(f"{sum//8:.1f}")