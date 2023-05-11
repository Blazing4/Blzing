#第一种方法
n=0
for a in range(101,201):
    for b in range(2,a):
        if a%b==0:
            break
        else:
            if b==a-1:
                print(a)
                n=n+1
print(n)