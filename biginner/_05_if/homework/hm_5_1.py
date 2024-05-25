#############
#这是5-1小节的课后作业第1题
#############
"""
条件测试：
编写一系列条件测试；
将每个测试以及你对其结果的预测和实际结果都打印出来。
你编写的代码应类似于下面这样：

·详细研究实际结果，直到你明白了它为何为True或False。
·创建至少10个测试，且其中结果分别为True和False的测试都至少有5个。
"""
##
#
## 列表展示
#
##

car = 'subaru'
print("Is car == 'subaru'?I predict True")
print(car == 'subaru')
print("\nIs car == 'audi'?I predict False")
print(car.upper() == 'audi')

print("\nIs car == 'SUBARU'?I predict True")
print(car.upper() == 'SUBARU')
print("\nIs car == 'Subaru'?I predict True")
print(car.title() == 'Subaru')
print("\nIs car == 'subaru'?I predict True")
print(car == 'subaru')
print("\nIs car != 'toyota'?I predict True")
print(car != 'toyota')
print("\nIs car != 'Toyota'?I predict True")
print(car != 'Toyota')

car = 'audi'
print("\nIs car == 'audi'?I predict False")
print(car.upper() == 'audi')
print("\nIs car == 'audi'?I predict False")
print(car.title() == 'audi')
print("\nIs car == 'Audi'?I predict False")
print(car.lower() == 'Audi')
print("\nIs car == 'AUDI'?I predict False")
print(car == 'AUDI')
print("\nIs car != 'audi'?I predict False")
print(car != 'audi')
