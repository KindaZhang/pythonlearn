#############
#这是7-1小节的课后作业第3题
#############
"""
10的整数倍：
让用户输入一个数字，
并指出这个数字是否是10的整数倍。
"""
##
#
## input() + %
#
##

number = input("请输入一个数字：")
number = int(number)
if number % 10 ==0:
    print("这个数是10的倍数")
else:
    print("这个数不是10的倍数")