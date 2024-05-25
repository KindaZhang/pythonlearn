#############
#这是4-4小节的课后作业第1题
#############
"""
切片：
选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
·打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
·打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
·打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
"""
##
#
## 切片
#
##



my_foods = ['pizza','falafel','carrot cake']
firend_foods = my_foods[:]
my_foods.append('cammoli')
firend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(firend_foods)
my_foods.append('ice cream')
print("The first three items in the list are:")
print(my_foods[:3])
print("Three items from the middle of the list are:")
print(my_foods[1:4])
print("The last three items in the list are:")
print(my_foods[-3:])
