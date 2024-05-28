
#############
#这是7-2小节的课后作业第3题
#############
"""
三个出口：
以另一种方式完成练习7-4或练习7-5，
在程序中采取如下所有做法。
·在while循环中使用条件测试来结束循环。
·使用变量active来控制循环结束的时机。
·使用break语句在用户输入'quit'时退出循环
"""
##
#
## break
#
##
toppings = input("输入pizza的配料：")
active = True
while active:
    toppings = input("输入pizza的配料：")
    if toppings == 'quit':
        break  
    else:
        print("我们会在pizza里面添加"+toppings)
        active = False