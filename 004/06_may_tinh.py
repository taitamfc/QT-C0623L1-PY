def cong(a,b):
    return a+b
def tru(a,b):
    return a-b
def nhan(a,b):
    return a*b
def chia(a,b):
    return a/b
a=int(input())
b=int(input())
chon=input('+,-,*,/ ')
if chon =='+':
    print(a,'+',b,'=',cong(a,b))
elif chon =='-':
    print(a,'-',b,'=',tru(a,b))
elif chon =='*':
    print(a,'*',b,'=',nhan(a,b))
elif chon =='/':
    print(a,'/',b,'=',chia(a,b))
else:
    print(' không đúng')
