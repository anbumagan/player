x=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if(i<x):
        c.append(i)
print(*(sorted(c)))
