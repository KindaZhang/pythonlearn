#############
#这是8-2小节的课后作业第2题
#############
"""
大号T恤：
修改函数make_shirt()，
使其在默认情况下制作一件印有字样“I love Python”的大号T恤。
调用这个函数来制作如下T恤：
一件印有默认字样的大号T恤、
一件印有默认字样的中号T恤和
一件印有其他字样的T恤（尺码无关紧要）。
"""
##
#
## 位置实参 默认值
#
##
def make_shirt(size,words='I love Python'):
    """打印T恤的尺寸和字样"""
    print("衬衫的尺寸是："+size)
    print("衬衫的字样是："+words)
print("第一件T恤：")
make_shirt('大',)
print("第二件T恤：")
make_shirt(size='中')
print("第三件T恤：")
make_shirt(size='小',words='I love C')