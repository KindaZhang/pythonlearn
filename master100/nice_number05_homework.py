#找出10000以内的**完美数**。
for i in range(2,10001):
    num = 0
    for x in range(1,i):
        if i % x == 0: 
            num += x
            #print(str(i)+' '+str(num))
    if i == num:
        print(i)