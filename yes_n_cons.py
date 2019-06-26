a,a1=map(int,input().split())
b=[]
for i in range(0,a):
    b.append(input())
for i in range(len(b)):
    c=0
    for j in range(i,len(b)):
        if(b[i]==b[j]):
            c=c+1
        else:
            break
if(c==a1):
    print("yes")
else:
    print("no")
