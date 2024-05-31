#############
#这是8-3小节的课后作业第3题
#############
"""
用户的专辑：
在为完成练习8-7编写的程序中，
编写一个while循环，
让用户输入一个专辑的歌手和名称。
获取这些信息后，
使用它们来调用函数make_album()，
并将创建的字典打印出来。
在这个while循环中，
务必要提供退出途径。
"""
##
#
## while 可选形参
#
##

def make_album(singer,name,songs=''):
    album = {'singer':singer,'name':name}
    if songs:
        album['songs'] = songs
    return album
print("输入'q'退出")
while True:
    singer = input("请输入歌手名称：")
    if singer == 'q':
        break
    name = input("请输入专辑名称：")
    if singer == 'q':
        break
    album = make_album(singer,name)
    print(album)
