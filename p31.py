x=str(input())
x1=list(x)
y=x1.count('(')
z=x1.count(')')
if(z==y):
    print("yes")
else:
    print("no")
