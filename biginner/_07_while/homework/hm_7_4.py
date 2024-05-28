#############
#这是7-2小节的课后作业第1题
#############
"""
比萨配料：
编写一个循环，
提示用户输入一系列的比萨配料，
并在用户输入'quit'时结束循环。
每当用户输入一种配料后，
都打印一条消息，
说我们会在比萨中添加这种配料。
"""
##
#
## 字典嵌套字典
#
##


toppings = input("输入pizza的配料：")
active = True
while active:
    toppings = input("输入pizza的配料：")
    if toppings == 'quit':
        active = False
    else:
        print("我们会在pizza里面添加"+toppings)
        
