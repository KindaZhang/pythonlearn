#############
#这是6-1小节的课后作业第2题
#############
"""
喜欢的数字：
使用一个字典来存储一些人喜欢的数字。
请想出5个人的名字，
并将这些名字用作字典中的键；
想出每个人喜欢的一个数字，
并将这些数字作为值存储在字典中。
打印每个人的名字和喜欢的数字。
为让这个程序更有趣，
通过询问朋友确保数据是真实的。
"""
##
#
## 类似对象组成的字典
#
##

favorite_numbers = {
    'zhang san':5,
    'li si':10,
    'wang wu':8,
    'liu qiang':96,
    'wang jian jun':100,
}
print("zhang san favorite number is "+str(favorite_numbers['zhang san']))
print("li si favorite number is "+str(favorite_numbers['li si']))
print("wang wu favorite number is "+str(favorite_numbers['wang wu']))
print("liu qiang favorite number is "+str(favorite_numbers['liu qiang']))
print("wang jian jun favorite number is "+str(favorite_numbers['wang jian jun']))