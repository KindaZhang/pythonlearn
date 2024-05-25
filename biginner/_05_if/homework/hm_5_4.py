#############
#这是5-3小节的课后作业第2题
#############
"""
外星人颜色#2：
像练习5-3那样设置外星人的颜色，
并编写一个if-else结构。
·如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
·如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
·编写这个程序的两个版本，在一个版本中执行if代码块，而在另一个版本中执行else代码块。
"""
##
#
## if-else语句
#
##

alien_color = 'green'
if alien_color == 'green':
    print("count:5,for shooting alien")
else:
    print("count:10,for shooting alien")
    
alien_color = 'blue'
if alien_color == 'green':
    print("count:5,for shooting alien")
else:
    print("count:10,for shooting alien")