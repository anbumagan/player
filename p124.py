a=int(input())
l=list(map(int,input().split()))
c=[]
d=[]
for i in range(1,1000):
    for j in l:
        if(i%j==0):
            c.append(i)
    if(c.count(i)==a):
        d.append(i)
print(d[0])
