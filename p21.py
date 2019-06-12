a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
if(a==c and a==e and c==e):
    print("yes")
elif(b==d and b==f and d==f):
    print("yes")
else:
    print("no")
       
