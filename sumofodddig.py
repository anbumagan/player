s=str(input())
a=0
for i in range(len(s)):
    if(int(s[i])%2!=0):
        a=a+int(s[i])
if(a%2==0):
    print("E")
else:
    print("O")
