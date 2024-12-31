a = input()
string1 = a[0]
string = a[0]
cnt = 0


for elem in a:
    if elem == string:
        cnt += 1
    
    else:
        string1 += str(cnt)
        string1 += elem
        cnt = 1
        string = elem

string1 += str(cnt)
print(len(string1))
print(string1)
        
