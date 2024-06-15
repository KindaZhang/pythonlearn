#生成**斐波那契数列**的前20个数。

first = 0
last = 1
i = 0
while i<20:
    temp = first
    first += last
    last = temp
    print(first)
    i += 1
    
    
#遇到的困难是，想把前面一个值付给后一个值的时候，没有temp时，再赋值输出结果就相当于平方了，
#如何采用中间变量后，好复赋值了，但是开头的两个1，不好弄，因为我一开始first=1last=0，
#后来欢乐就出现了
"""
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
"""

#