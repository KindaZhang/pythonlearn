#############
#这是4-3小节的文中代码
#############
##
#
## 数值列表
#
##

#range()函数
for value in range(1,5):
    print(value)

#list()创建列表
numbers = list(range(1,6))
print(numbers)

#步长 even_numbers.py
even_numbers = list(range(2,11,2))
print(even_numbers)

#平方** squares.py
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
    
#数值运算
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))   
print(max(digits)) 
print(sum(digits)) 
    
    

#列表解析  squares.py
squares = [value**2 for value in range(1,11)]
print(square)







 
#range()函数，两个参数，开始数字，结束数字，取值[开始数字，结束数字），正整数
#第三个参数--步长，指的是两个数字的间隔
# ** 代表的是平方
# 计算 min()最小值 max()最大值 sum()求和