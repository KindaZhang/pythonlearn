#############
#这是3-3小节的文中代码
#############
##
#
## sort()
#
##

#永久排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#临时排序
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#翻转列表
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

#列表长度
cars = ['bmw','audi','toyota','subaru']
print(len(cars))




#sort()函数是排序，按从小到大排序，升序
#永久改变排列顺序 
#参数reverse默认是false，升序；true，降序；
#sorted()临时排序，列表并未改变，参数和sort()一样
#reverse()翻转列表，两次调用回复原状
#翻转也是永久改变
#len()列表长度计算