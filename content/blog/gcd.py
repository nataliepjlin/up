def gcd(a,b):
    while(1):
        r=a%b
        a=b
        b=r
        if r==0:
            return a
            break
def gcd2(a,b):
    if(b==0):
        print("finala=",a," finalb=",b)
        return a
    else:
        print("nowa=",a," nowb=",b)
        return gcd2(b,a%b)


print(gcd2(420,66))
print(gcd2(1071,462))


