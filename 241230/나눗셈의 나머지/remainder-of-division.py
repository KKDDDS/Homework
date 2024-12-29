a, b = map(int, input().split())
arr = [a]

rst = [0]*4
for i in arr:
    if i>1:
        k = i%b
        rst[k] += 1
        n = i//b
        arr.append(n)

    
sum = 0
for num in rst:
    sum += num**2

print(sum)