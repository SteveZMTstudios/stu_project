def is_returnword(pin):
    nip=pin[::-1]
    if pin==nip:
        return True
    else:
        return False


def is_onlynum(pin):
    for j in range(2,pin-1):
        if pin%j==0:
            return False
    return True
        
import os
input_range_mx=int(input("Enter an number(int) to calc.ヾ(≧▽≦)*o\n]"))
for swing in range(2,input_range_mx):
    if is_returnword(str(swing)) and is_onlynum(swing):
        print(swing)
os.system("pause")
