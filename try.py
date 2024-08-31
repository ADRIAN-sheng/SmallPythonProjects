n = 12
a = 1
b = 1

if n ==1 or n==2:
    print(1)
else:
    for i in range(3,n+1):
        r=a+b
        a,b = b,r
    print(r)