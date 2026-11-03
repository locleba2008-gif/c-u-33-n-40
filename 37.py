def UCLN(a,b):
    while b!=0:
        a,b=b,a%b
    return a

m,n=map(int, input('').split())
tu_so=int(m/UCLN(m,n))
mau_so=int(n/UCLN(m,n))
print(tu_so,mau_so,sep='/')