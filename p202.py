a=str(input())
v=['a','e','i','o','u']
c=""
d=""
for i in range(len(a)):
    if(a[i] in v):
        c=c+a[i]
    else:
        d=d+a[i]
print(c+d)
