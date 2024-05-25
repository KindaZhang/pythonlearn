#############
#这是4-4小节的文中代码
#############
##
#
## 列表操作
#
##

#切片
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#遍历切片
players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#复制列表 foods.py
my_foods = ['pizza','falafel','carrot cake']
firend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(firend_foods)

my_foods = ['pizza','falafel','carrot cake']
firend_foods = my_foods[:]
my_foods.append('cammoli')
firend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(firend_foods)

#这不是复制，是赋值
"""
my_foods = ['pizza','falafel','carrot cake']
firend_foods = my_foods
my_foods.append('cammoli')
firend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(firend_foods)
"""





#切片[a,b]注意取值[a ,b ),其中a省略时代表从第一位开始，当b省略时代表渠道最后一位
#a b可以为负数，列表一开始有讲
#a b全部省略时即[:]就是复制