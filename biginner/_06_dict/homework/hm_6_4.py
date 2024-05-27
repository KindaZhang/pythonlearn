#############
#这是6-3小节的课后作业第1题
#############
"""
词汇表2：
既然你知道了如何遍历字典，
现在请整理你为完成练习6-3而编写的代码，
将其中的一系列print语句替换为一个遍历字典中的键和值的循环。
确定该循环正确无误后，
再在词汇表中添加5个Python术语。
当你再次运行这个程序时，
这些新术语及其含义将自动包含在输出中。
"""
##
#
## items()
#
##


words = {
    'list()':'生成列表',
    'str()':'强制转换数据类型为字符串',
    'sorted()':'临时排序',
    'range()':'生成数字',
    'len()':'数据长度',
    }
print("\nlist():"+words['list()'])
print("\nstr():"+words['str()'])
print("\nsorted():"+words['sorted()'])
print("\nrange():"+words['range()'])
print("\nlen():"+words['len()']+"\n")
words['sort()'] = '永久排序'
words['int()'] = '强制转换数据类型为整型'
words['set()'] = '去重且创建一个合集'
words['items()'] = '返回键值对列表'
words['keys()'] = '返回键列表'
for key,value in words.items():
    print(key+":")
    print(value)