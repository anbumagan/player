a=int(input())
l=list(map(int,input().split()))
c=[]
a=[[l.count(i),i]for i in l]
a=sorted(a)
a=a[::-1]
for j in a:
     if(j[1] not in c):
        c.append(j[1])
print(*c)
