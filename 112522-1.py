def step_ext(target):#递归实例
    if target==1:
        return 1
    #定义递归边界
    return step_ext(target-1)*target#递归主体

def f(x,n):
    s=x
    
    for i in range(2,n+1):
        s+=x**n/step_ext(n)

    return s
import os
os.system('color 9f')
os.system('title Python Demo')
print("The answer is:",f(int(input("Enter an number(int) to run this demo program(X)ヾ(≧▽≦)*o\n>>>")),int(input("Enter an number(int) to run this demo program(N) q(≧▽≦)q\n>>>"))))
print("Program Complete!Press Enter key to exit.")
os.system('color af')
input()
#ヾ(≧▽≦)*o
#q(≧▽≦)q
