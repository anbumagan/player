x,y=map(int,input().split())
l=[]
for i in range(x,y+1):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if(c==2):
        l.append(x)
print(len(l))  
