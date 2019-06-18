a=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(0,a-1,2):
    l[i],l[i+1]=l[i+1],l[i]
        
print(*l) 
