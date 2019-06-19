l=list(map(int,input().split("/")))
if(l[0]<=31 and l[1]<=12 and len(str(l[2]))==4):
    print("yes")
else:
    print("no")
