x,y=map(int,input().split())
l=list(map(int,input().split()))
c=[]
for i in l:
    if(i<y):
        c.append(i)
print(*(sorted(c)))
