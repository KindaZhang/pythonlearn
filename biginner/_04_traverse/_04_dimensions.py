#############
#这是4-5小节的文中代码
#############
##
#
## 元组
#
##



#初识元组
dimensions = (2000,50)
print(dimensions[0])
#dimensions[0] = 250
print(dimensions[1])


#遍历元组
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)


#修改元组变量
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)






#元组与列表区别： 1、列表可以修改，元组不可以更改 2、列表表示[,,],元组表示() 3、列表为空[]，元组为空(,)
#元组不可以更改，但可以赋值