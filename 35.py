def so_nguyen_to(a):
    if a==1:
        return False
    elif a>1:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
    return True


m,n=map(int, input('').split())
sum_so_nguyen_to=0
count=0
for i in range(m,n+1):
    if so_nguyen_to(i):
        sum_so_nguyen_to+=i
        count+=1
TBC=sum_so_nguyen_to/count  
print(f'{TBC:.2f}')