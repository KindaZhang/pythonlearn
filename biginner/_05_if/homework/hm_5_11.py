#############
#这是5-4小节的课后作业第4题
#############
"""
序数：
序数表示位置，如1st和2nd。
大多数序数都以th结尾，只有1、2和3例外。
·在一个列表中存储数字1～9。·遍历这个列表。
·在循环中使用一个if-elif-else结构，
以打印每个数字对应的序数。
输出内容应为1st、2nd、3rd、4th、5th、6th、7th、8th和9th，
但每个序数都独占一行。
"""
##
#
## if-elif-else语句
#
##

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number =='1':
        print(number+"st")
    elif number =='2':
        print(number+"nd")
    elif number =='3':
        print(number+"rd")
    else:
        print(str(number)+"th")
    
    
#理解，为什么地29行要加str，别的地方不需要加
#因为print只能打印一种类型，而前面的number对比的是字符串，如果将123的引号去除，那么打印的number也要进行类型强制转换

