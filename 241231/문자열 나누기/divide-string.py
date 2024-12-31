n = int(input())
string = list(map(str,input().split()))

ttl_string = ''
for elem in string:
    ttl_string += elem
cnt = ''
for i in range(1,len(ttl_string)+1):
    cnt += ttl_string[i-1]
    
    if i%5 == 0:
        print(cnt)
        cnt = ''
if cnt != '':
    print(cnt)