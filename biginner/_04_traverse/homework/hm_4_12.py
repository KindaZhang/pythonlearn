#############
#这是4-4小节的课后作业第3题
#############
"""
使用多个循环：
在本节中，为节省篇幅，
程序foods.py的每个版本都没有使用for循环来打印列表。
请选择一个版本的foods.py，在其中编写两个for循环，
将各个食品列表都打印出来。
"""
##
#
## for
#


my_foods = ['pizza','falafel','carrot cake']
firend_foods = my_foods[:]
my_foods.append('cammoli')
firend_foods.append('ice cream')
print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)
print("\nMy friend's favorite foods are:")
for friend_food in firend_foods:
    print(friend_food)




#错误点 打印了五个列表