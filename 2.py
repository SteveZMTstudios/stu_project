def f(n):
    a,b=0,1
    x=0
    for i in range(n):
        a,b=b,a+b
        x+=1
    return a

print(f(10))
input()
