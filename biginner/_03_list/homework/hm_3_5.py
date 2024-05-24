#############
#这是3-2小节的课后作业第2题
#############
"""
修改嘉宾名单：
你刚得知有位嘉宾无法赴约，
因此需要另外邀请一位嘉宾。
·以完成练习3-4时编写的程序为基础，在程序末尾添加一条print语句，指出哪位嘉宾无法赴约。
·修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
·再次打印一系列消息，向名单中的每位嘉宾发出邀请。
"""
##
#
## 列表使用, pop() insert()
#
##

inventer = ['zhangyishan','liuyifei','sunqian']
leave_inventer = inventer.pop(1)
print(leave_inventer+" can not attend")
inventer.insert(1,'yangmi')
message = 'welcome to my party,'
print(message+inventer[0])
print(message+inventer[1])
print(message+inventer[2])


#错误点leave_inventer = inventer[1].pop()
#错误点在指定位置所以不可以用append()
#错误点在使用pop函数后，列表只有俩个元素，所以不可以用直接赋值进行元素插入，出现列表元素缺失