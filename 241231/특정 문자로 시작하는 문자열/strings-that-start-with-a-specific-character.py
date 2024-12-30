n = int(input())
arr = []
cnt = 0
sum = 0
for i in range(n):
    arr.append(input())

s = input()

for elem in arr:
    if elem[0] == s:
        cnt += 1
        sum += len(elem)

print(f"{cnt} {sum/cnt:.2f}")
