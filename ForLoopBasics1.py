for i in range(0, 151):
    print(i)
for x in range(5,1001,5):
    print(x)
for y in range(1,101):
    if y%10==0:
        print('coding dojo')
    elif y%5==0:
        print("coding")
    else:
        print(y)
sum = 0
for n in range(1, 500000):
    if n%2 != 0:
        sum=sum+n
        print(sum)
for m in range(2018, 0, -4):
    print(m)
lowNum=2
highNum=10
mult=3
for q in range(lowNum, highNum):
    if q%mult==0:
        print(q)