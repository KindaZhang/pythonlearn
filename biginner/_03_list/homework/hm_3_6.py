#############
#这是3-2小节的课后作业第3题
#############
"""
添加嘉宾：
你刚找到了一个更大的餐桌，
可容纳更多的嘉宾。
请想想你还想邀请哪三位嘉宾。
·以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print语句，指出你找到了一个更大的餐桌。
·使用insert()将一位新嘉宾添加到名单开头。
·使用insert()将另一位新嘉宾添加到名单中间。
·使用append()将最后一位新嘉宾添加到名单末尾
·打印一系列消息，向名单中的每位嘉宾发出邀请。
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