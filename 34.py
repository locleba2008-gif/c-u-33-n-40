def so_nguyen_to(a):
    if a==1:
        return False
    elif a>1:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
    return True


m,n=map(int, input('').split()) 
for i in range(m,n+1):
    if so_nguyen_to(i):
        print(i, end=' ')