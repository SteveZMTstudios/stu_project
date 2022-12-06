def yhwg(x,y):

    if x>20:
        x-=20
        m=x*(y*0.15)
        m=round(m,2)
    else:
        m=0
    return m

weight=int(input("行李重量\n]"))
price=int(input("机票价格\n]"))

print("超重量行李费用:",yhwg(weight,price)," CHN")
