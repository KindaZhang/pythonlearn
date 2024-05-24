#############
#这是4-1 4-2小节的文中代码
#############
##
#
## for循环
#
##

#for循环1
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
    
#2
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title()+",that was a great triick!")
    
#3   
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title()+",that was a great triick!")
    print("I can't wait to see your next trick,"+magician.title()+".\n")
 
#缩进4  
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title()+",that was a great triick!")
    print("I can't wait to see your next trick,"+magician.title()+".\n")
print("Thank you,everyone.That was a great magic show!")


#缩进错误 报错 语法错误
"""
magicians = ['alice','david','carolina']
for magician in magicians:
print(magician) 
"""
#额外缩进错误 不报错 逻辑错误
"""
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title()+",that was a great triick!")
print("I can't wait to see your next trick,"+magician.title()+".\n")
"""
#无需缩进 报错
"""
message = "Hello Python world!"
    print(message)
"""

#不必要的缩进错误 不报错 逻辑错误
"""
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title()+",that was a great triick!")
    print("I can't wait to see your next trick,"+magician.title()+".\n")
    print("Thank you,everyone.That was a great magic show!")
"""

#漏打冒号 语法错误 报错
"""
magicians = ['alice','david','carolina']
for magician in magicians
    print(magician)
    
"""

#for循环，在magicians内取出元素存在变量magician中，然后打印变量的值
#变量的名字可以任意取，但一般取的比较有意义
#不需要和c一样的大括号，用缩进代替大括号，即缩进的内容是循环的一部分