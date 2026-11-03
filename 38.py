# Kiểm tra số nguyên tố
def so_nguyen_to(a):
    if a<2:
        return False
    elif a>1:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
    return True

#In số nguyên tố
k=int(input(''))
n=2
dem=1
while dem<k+1:
    if so_nguyen_to(n):
        dem+=1
        print(n, end=' ')
    n+=1    