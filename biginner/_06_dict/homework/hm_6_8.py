#############
#这是6-4小节的课后作业第2题
#############
"""
宠物：
创建多个字典，
对于每个字典，
都使用一个宠物的名称来给它命名；
在每个字典中，
包含宠物的类型及其主人的名字。
将这些字典存储在一个名为pets的列表中，
再遍历该列表，
并将宠物的所有信息都打印出来。
"""
##
#
## 字典
#
##
alien = {'variety':'cat','master':'小张'}
alice = {'variety':'dog','master':'小王'}
boobo = {'variety':'rabbit','master':'小李'}
pets = [alien,alice,boobo]
for pet in pets:
    print("宠物种类：")
    print(pet['variety'])
    print("宠物的主人：")
    print(pet['master'])