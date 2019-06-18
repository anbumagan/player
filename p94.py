a=str(input())
c=0
for i in range(0,len(a)):
    for k in range(i+1,len(a)):
        if(a[i]==a[k]):
            c=c+1 
if c >= 1:
    print("yes")
else:
    print("no")
