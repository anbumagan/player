a2=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(a2):
    c.append([b[i],a[i]])
c.sort()
for i in c:
    print(i[1],end=" ")
