x,y=map(int,input().split()) 
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    k=l[i]
    for j in range(1,len(l)+1):
        if((k+j)==y):
            c=c+1 
if(c>=1):
    print("yes")
else:
    print("no")
