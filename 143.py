a2=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(a2):
    c.append([b[i],a[i]])
c.sort()
c=c[::-1]
for i in c:
    print(i[1],end=" ")
