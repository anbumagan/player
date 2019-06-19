n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    s.append(l.index(i)+1)
print(*s[::-1])
