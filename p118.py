a=list(map(str,input().split()))
c=[]
for i in range(len(a)-1):
    if(len(a[i])==len(a[i+1])):
        c.append(a[i])
if(len(c)==0):
    print(max(a))
else:
    print(c[0])
