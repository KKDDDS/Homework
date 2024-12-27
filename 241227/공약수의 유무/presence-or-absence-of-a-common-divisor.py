a, b  = map(int, input().split())
ans = False
for i in range(a, b+1):
    if 1920%i ==0 or 2880%i ==0:
        ans = True

if ans == True:
    print(1)
else:
    print(0)
