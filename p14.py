n=input()
str=input()
lis=list(str)
f=[]
l=['a','e','i','o','u']
for i in (lis):
    if i not in l:
        f.append(i)
g="".join(f)
print(g[::-1])
