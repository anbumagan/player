num=int(input())
j=list(map(int,input().split()))
c={}
s=[]
for i in j:
    y=j.count(i)
    c[i]=y
    if(c[i]==1):
        print(i)
