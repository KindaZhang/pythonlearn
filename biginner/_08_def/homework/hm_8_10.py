#############
#这是8-4小节的课后作业第2题
#############
"""
了不起的魔术师：
在你为完成练习8-9而编写的程序中，
编写一个名为make_great()的函数，
对魔术师列表进行修改，
在每个魔术师的名字中都加入字样“the Great”。
调用函数show_magicians()，
确认魔术师列表确实变了。
"""
##
#
## 
#
##
magicians = ['Harry Houdini','David Copperfield','Merlin']
great_magicians = []
def show_magicians():
    for magician in great_magicians:
        print(magician.title())

def make_great():
    while magicians:
        magician = magicians.pop()
        magician = "the great "+magician
        great_magicians.append(magician)  
make_great()
show_magicians()