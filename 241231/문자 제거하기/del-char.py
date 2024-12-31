a = list(input())

while len(a)>1:
    s = int(input())
    if s < len(a):
        a.pop(s)
    else:
        a.pop(-1)
    
    ans = ''.join(a)
    print(ans)