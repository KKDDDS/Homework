a = list(input())
b = list(input())

while True:
    found = False  
    for i in range(len(a) - len(b) + 1): 
        if a[i:i+len(b)] == b:
            del a[i:i+len(b)]
            found = True 
            break
    if not found:
        break

ans = ''.join(a)  # 리스트를 문자열로 변환
print(ans)
                