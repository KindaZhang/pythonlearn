#############
#这是7-2小节的课后作业第2题
#############
"""
电影票：
有家电影院根据观众的年龄收取不同的票价：
不到3岁的观众免费；
3～12岁的观众为10美元；
超过12岁的观众为15美元。
请编写一个循环，
在其中询问用户的年龄，
并指出其票价。
"""
##
#
## int()
#
##

active = True
while active:
    age = input("输入你的年龄：")
    age = int(age)
    if age < 3:
        print("免费")
        active = False
    elif age > 12:
        print("票价15美元")
        active = False
    else:
        print("票价10美元")
        active = False