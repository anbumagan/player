a1=int(input())
e=[]
for i in range(2,a1):
    if(a1%i==0):
        d=0
        for j in range(1,i+1):
            if(i%j==0):
                d=d+1
        if(d==2):
            e.append(j)
print(*sorted(e))
