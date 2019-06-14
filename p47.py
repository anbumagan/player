x,z,y=map(int,input().split())
if(x!=0 and y!=0 and z!=0):
    if((x+y+z)==180):
        print("yes")
    else:
        print("no")
else:
    print("no")

