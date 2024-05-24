#############
#这是3-1小节的课后作业第1题
#############
"""
晚餐嘉宾：
在完成练习3-4～练习3-7时编写的程序之一中，
使用len()打印一条消息，
指出你邀请了多少位嘉宾来与你共进晚餐。
"""
##
#
## 列表函数 len()
#
##

inventer = ['zhang yi shan','liu yi fei','sun qian']
leave_inventer = inventer.pop(1)
print(leave_inventer+" can not attend")
inventer.insert(1,'yang mi')
message = 'welcome to my party,'
print(message+inventer[0])
print(message+inventer[1])
print(message+inventer[2])

print("I find a bigger table")
inventer.insert(0,'di li re ba')
inventer.insert(2,'gu li na zha')
inventer.append('xie na')
print("welcome to my party,"+inventer[0])
print("welcome to my party,"+inventer[1])
print("welcome to my party,"+inventer[2])
print("welcome to my party,"+inventer[3])
print("welcome to my party,"+inventer[4])
print("welcome to my party,"+inventer[5])

print("I am sorrry that I only can invent two friend to my party")
inventer.pop()
print("I am sorry.I will invent you next time")
inventer.pop()
print("I am sorry.I will invent you next time")
inventer.pop()
print("I am sorry.I will invent you next time")
inventer.pop()
print("I am sorry.I will invent you next time")
print("you can come to my party"+inventer[0].title())
print("you can come to my party"+inventer[1].title())
del inventer[0]
del inventer[0]
print(inventer)
print(len(inventer))