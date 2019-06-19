n=int(input())
l=list(map(int,input().split()))
s=[]
if(l==sorted(l)):
    for i in l:
        s.append(l.index(i)+1)
    print(*s)
else:
    for i in l:
        s.append(l.index(i)+1)
    print(*s[::-1]) 
