n=int(input())
for i in range(2,n+1):
    if(n%i==0):
        c=0
        for k in range(1,i+1):
            if(i%k==0):
                c=c+1
        if(c==2):
            print(k,end=" ")
        
