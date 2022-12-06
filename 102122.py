year=int(input("请输入年份:"))
s1="庚辛壬癸甲乙丙丁戊己"
s2="申酉戌亥子丑寅卯辰已午未"
a=year%10
b=year%12
c=s1[a]+s2[b]
print("天干地支为:",c)
