#############
#这是4-3小节的课后作业第4题
#############
"""
3的倍数：
创建一个列表，
其中包含3～30内能被3整除的数字；
再使用一个for循环将这个列表中的数字都打印出来。
"""
##
#
## range()步长 列表
#
##
numbers = []
for number in range(3,31,3):
    numbers.append(number)
for number in numbers:
    print(number)