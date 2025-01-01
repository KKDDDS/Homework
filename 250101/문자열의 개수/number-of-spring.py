ans = True
cnt = 0
arr = []
while ans:
    string = input()
    if string =='0':
        ans = False
    else:
        cnt += 1
        arr.append(string)

print(cnt)

for i in range(len(arr)):
    if i%2==0:
        print(arr[i])
        