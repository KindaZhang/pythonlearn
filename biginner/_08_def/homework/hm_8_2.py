#############
#这是8-1小节的课后作业第2题
#############
"""
喜欢的图书：
编写一个名为favorite_book()的函数，
其中包含一个名为title的形参。
这个函数打印一条消息，
如One of my favorite books is Alice inWonderland。
调用这个函数，
并将一本图书的名称作为实参传递给它。
"""
##
#
## 形参
#
##

def favorite_book(title):
    """打印消息"""
    print("One of my favorite books is "+title.title())
favorite_book('alice in wonderland')