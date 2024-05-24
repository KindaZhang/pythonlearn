#############
#这是3-2小节的文中代码
#############
##
#
## list的增删改查
#
##

#列表
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#列表表尾添加
motorcycles.append('ducati2')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('yamaha')
motorcycles.append('ducati2')
print(motorcycles)
#列表指定位置添加
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

#列表指定位置删除 del
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
del motorcycles[1]
print(motorcycles)

#列表默认表尾删除 删除内容可以引用 pop
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#末尾删除 引用
motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned waws a "+last_owned.title()+".")
#指定位置删除
motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop(0)
print("The last motorcycle I owned waws a "+last_owned.title()+".")

#根据值删除元素,可以引用该值
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)


motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")

#用赋值的方法改变列表的元素
#append()将元素添加列表末尾，也可以创建一个空列表在进行添加元素
#insert()函数，有两个参数，第一个参数是索引，第二个参数是添加内容,后面元素自动顺延
#del可以删除指定位置的元素
#pop()从末尾弹出元素，而且可以引用弹出元素，在括号内添加索引，既可以删除指定元素
#del和pop的区别就是是否再次使用弹出的元素
#remove()删除指定值，但只删除第一个指定的值