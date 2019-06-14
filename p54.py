a,b=map(str,input().split())
if(len(a)==len(b)):
    c=len(a)
    for i in range(0,len(a)):
        if(a[i]==b[i]):
            c=c-1
    if(c==0):
        print("yes")
    else:
        print("no")
else:
    print("no")
