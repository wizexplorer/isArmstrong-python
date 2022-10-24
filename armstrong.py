print("|-------------------------EXPERIMENT NO.17-----------------------------|")
print("|            CHECKING IF THE NUMBER IS ARMSTRONG OR NOT                |")
print("|----------------------------------------------------------------------|")
num=input("                  Enter a number : ")
print("*"*72)
nnum = num[:]
total=0
n=len(num)-1
num=int(num)
while n>=0:
    digit=num//10**n
    num=num%10**n
    total=total+digit**3
    n-=1
if str(total)==nnum:
    print("*                                 ",nnum,"is Armstrong                    *")
else:
    print("*                                 ",nnum,"is not Armstrong                *")
print("*"*72)
