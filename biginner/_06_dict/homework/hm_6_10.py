#############
#这是6-4小节的课后作业第4题
#############
"""
喜欢的数字：
修改为完成练习6-2而编写的程序，
让每个人都可以有多个喜欢的数字，
然后将每个人的名字及其喜欢的数字打印出来。
"""
##
#
## 字典嵌套列表
#
##

favorite_numbers = {
    '张三':[5,7],
    '李四':[10,13,35],
    '王五':[8],
    '刘强':[96,99,90,12],
    '王建军':[100,108,180],
}
for name,favorite_number in favorite_numbers.items():
    print(name+"最喜欢的数字是：")
    for numbers in favorite_number:
        print(numbers)
