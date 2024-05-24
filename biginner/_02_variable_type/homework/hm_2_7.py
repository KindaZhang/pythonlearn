#############
#这是2-3小节的课后作业第五题
#############
"""
剔除人名中的空白：
存储一个人名，
并在其开头和末尾都包含一些空白字符。
务必至少使用字符组合"\t"和"\n"各一次。
打印这个人名，
以显示其开头和末尾的空白。
然后，
分别使用剔除函数lstrip()、
rstrip()和strip()对人名进行处理，
并将结果打印出来。
"""
##
#
## 利用函数去除空白
#
##

name = " \teric\nert "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())