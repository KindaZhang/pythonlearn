# day05总结

## 文中代码

<p>1、寻找**水仙花数**。

> **说明**：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：1^3 + 5^3+ 3^3=153。

```python
for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 +mid ** 3 + high ** 3:
        print(num)
```

总结：range(num1,num2)生成数字，数字的取值区间是[num1,,num2) .取余% --举例：10%3 = 1，取余数。整除// --举例：10//3 =3,是个整数，如果是除/那就会有小数点。

<p>数字的翻转

```python
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
```

<P>**百钱百鸡**问题。

> **说明**：百钱百鸡是我国古代数学家[张丘建](https://baike.baidu.com/item/%E5%BC%A0%E4%B8%98%E5%BB%BA/10246238)在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

```python
for x in range(0, 100):
    for y in range(0, 103):
        for z in range(0, 100):
            if 5 * x + 3 * y + z/3 == 100 and x + y + z == 100:
                print("公鸡数量："+str(x)+" 母鸡数量："+str(y)+" 小鸡数量："+str(z))


"""
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
            """
```

总结：上面的是我写的，一开始看漏了条件（ x + y + z == 100），所以没有出来结果。主要学习的是：print语句的表达

```python
        print("公鸡数量："+str(x)+" 母鸡数量："+str(y)+" 小鸡数量："+str
        print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' 
```

### print语句使用

语法：

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

> - objects --输出的对象，可以是多个对象，用逗号隔开
> 
> - sep -- 用来间隔多个对象，默认是空格
> 
> - end -- 结尾是什么，默认是换行（\n）
> 
> - file --需要写入的文件对象
> 
> - flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新

```python
print('hello')
hello
print('hello','boy')
helloboy
print('hello','boy',sep='')
hello boy
print('hello','boy',sep='!!!')
hello!!!boy
print('hello','boy',sep='',end='!!!')
hello boy!!!
```

**%d** -- 整数，**%s** --字符串，**%f** --小数，**%num1.num2f** --num1表示输出的长度，num2表示小数点后保留几位

<p>**CRAPS赌博游戏**。

> **说明**：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。

```python
from random import randint
#CRAPS赌博游戏 本钱：1000
money = 1000
while money > 0:   #持续进行知道无本钱
    
    print('你得总资产为：',money) #每次运行后查看本钱
    needs_go_on = False          #控制其他点数是否玩的状态
    while True:                  #确保下注金额，循环是保证真的下注
        debt = int(input('请下注：')) 
        if 0 < debt <= money:
            break
    first = randint(1,6) +randint(1,6) #第一次掷色子，我本来想的是如何两次如何掷色子，因为，分开来就不好继续进行
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11: #第一次玩家胜利
        print('玩家胜！')
        money += debt              #赌钱增加押注
    elif first == 2 or first == 3 or first == 12:#庄家胜
        print('庄家胜！')
        money -= debt#玩家本钱减少
    else:
        needs_go_on = True
    while needs_go_on:  #其他点数继续玩
        needs_go_on = False
        current = randint(1,6)+randint(1,6)
        print('玩家摇出了%d点'% current)
        if current == 7:
            print('庄家胜！')
            money -= debt
        elif current == first:
            print('玩家胜！')
            money += debt
        else:
            needs_go_on = True
print('你破产了，游戏结束！')
```

总结：needs_go_on = True,这个思想的学习。

## 练习

生成**斐波那契数列**的前20个数。

> **说明**：斐波那契数列（Fibonacci sequence），又称黄金分割数列，是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，所以这个数列也被戏称为"兔子数列"。斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。

```python
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

#练习答案
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')

#a, b = b, a + b 这个是赋值语句相当于 a=b b+=a，但是这两句不行，我试过，值会变的，需要中间值，就是我采用的方法


#
```

找出10000以内的**完美数**。

> **说明**：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。例如：6（6=1+2+3）和28（28=1+2+4+7+14）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。

```python
for i in range(2,10001):
    num = 0
    for x in range(1,i):
        if i % x == 0: 
            num += x
            #print(str(i)+' '+str(num))
    if i == num:
        print(i)
#如果将第二个if放入第二个循环，会出现其他情况，譬如24，在24 = 1+2+3+4+6+8，
#这时仍有12未加入，此时需要进行判断，但条件又不好添加

#练习答案
import math

for num in range(2, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)

#第二个for循环，将i开方，因为range取值娶不到开方的数，所以需要加1，--举例25开方为5，range
#range第二个数为6时才可以取到5
#第二个if语句，factor取值大于1，且通过了第一个语句，所以肯定有另一个大一点的数，使得链各个数想成等于num
#if的第二个条件意思是怕平方，如果是平方，第一个已经加过了，不能再加一遍




#
```

输出**100以内所有的素数**。

> **说明**：素数指的是只能被1和自身整除的正整数（不包括1）。

```python
for i in range(2,101):
    needs_go_on = True
    for x in range(2,i+1):
        if i % x == 0 and i != x:
            needs_go_on = False
            break
    if needs_go_on:
        print('%d是素数' % i)
#布尔值的应用

import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')

#设置bool值，如果能被其他数整除，那么就开始下一个循环，如果没有被整除，bool值就没有改变
#就可以运行下一个if语句了。注意bool值放再循环内，否则除了输出2 3 外boo值就一直为False







#
```

## 总结

1、取余 **%** 整除 **//** 除 **/** 的运用

2、**print**语句的使用

3、**布尔值**的使用


