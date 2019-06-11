m=int(input())
l=[]
s=set("kabali")
d=0
for i in range(1,m+1):
    n=input()
    l.append(n)
c=0    
for i in range(len(l)):
        c=set(l[i])
        if(s==c):
            d=d+1

print(d)
