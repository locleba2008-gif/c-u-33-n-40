def UCLN(a,b):
    while b!=0:
        a,b=b,a%b
    return a

m,n=map(int, input('').split())
print(UCLN(m,n))