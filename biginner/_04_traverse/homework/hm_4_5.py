#############
#这是4-3小节的课后作业第3题
#############
"""
奇数：
通过给函数range()指定第三个参数来创建一个列表，
其中包含1～20的奇数；
再使用一个for循环将这些数字都打印出来。
"""
##
#
## range()步长 列表
#
##

odd = []
for number in range(1,21,2):
    odd.append(number)
    print(number)
print(odd)