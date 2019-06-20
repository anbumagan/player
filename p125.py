a=int(input())
l=list(map(int,input().split()))
d=[]
for i in range(1,max(l)+1):
    c=0
    for j in range(0,a):
        if(l[j]%i==0):
            c=c+1
        if(c==a):
             d.append(i)
print(max(d))
