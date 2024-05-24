#############
#这是3-2小节的课后作业第2题
#############
"""
缩减名单：
你刚得知新购买的餐桌无法及时送达，
因此只能邀请两位嘉宾。
·以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
·使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
·对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
·使用del将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
"""
##
#
## 列表使用, insert()append()
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


#错误点 del连用时注意列表索引