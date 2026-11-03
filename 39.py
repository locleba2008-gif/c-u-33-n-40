def kiem_tra_so_chinh_phuong(n):
    if (int(n**0.5))**2==n:
        return True
    else:
        return False

n=int(input(''))
if kiem_tra_so_chinh_phuong(n):
    print('Yes')
else:
    print('No')        