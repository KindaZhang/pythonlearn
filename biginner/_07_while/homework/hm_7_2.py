#############
#这是7-1小节的课后作业第2题
#############
"""
餐馆订位：
编写一个程序，
询问用户有多少人用餐。
如果超过8人，
就打印一条消息，
指出没有空桌；
否则指出有空桌。
"""
##
#
## input()int()
#
##
people = input("How many people want to eat?")
people = int(people)
if people >= 8:
    print("Tables are not enough!")
else:
    print("There are tables!")