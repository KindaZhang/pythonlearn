#############
#这是4-4小节的课后作业第2题
#############
"""
你的比萨和我的比萨：
在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其存储到变量friend_pizzas中，再完成如下任务。
·在原来的比萨列表中添加一种比萨。
·在列表friend_pizzas中添加另一种比萨。
·核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个for循环来打印第一个列表；
打印消息“My friend's favorite pizzas are:”，再使用一个for循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
"""
##
#
## 切片 for
#
##
pizzas = ['seafood pizza','cheese pizza','beef pizza']
for pizza in pizzas:
    print(pizza)
    print("I like "+pizza+".")
print("I really love pizza!")
friend_pizzas = pizzas[:]
pizzas.append("fruit pizza")
friend_pizzas.append("pork pizza")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)