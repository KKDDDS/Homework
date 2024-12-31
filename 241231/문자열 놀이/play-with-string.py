s,q = input().split()
s = list(s)
q = int(q)

for i in range(q):
    qs = list(input().split())
    if qs[0] == '1':
        s1 = int(qs[1])
        s2 = int(qs[2])
        temp = s[s1-1]
        s[s1-1] = s[s2-1]
        s[s2-1] = temp

        ans = ''.join(s)
        print(ans)

    elif qs[0] =='2':

        a = qs[1]
        b = qs[2]
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
        ans = ''.join(s)
        print(ans)
