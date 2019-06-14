x=int(input())
c=[]
for i in range(1,100000):
    if(x%i==0):
        if((x//i)%2!=0):
            c.append(i)
print(min(c)) 
