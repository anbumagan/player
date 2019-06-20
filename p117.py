a=str(input())
a=a[::-1]
c=[]
for i in range(len(a)):
    c.append(a[i])
    c.append("-")
d="".join(c[:len(c)-1])
print(d)
