#############
#这是7-3小节的课后作业第3题
#############
"""
梦想的度假胜地：
编写一个程序，
调查用户梦想的度假胜地。
使用类似于“If you could visit one place in the world,where would you go?”的提示，
并编写一个打印调查结果的代码块
"""
##
#
## 
#
##

question = "If you could visit one place in the world,where would you go?"
#question+= "\nEnter 'quit' to leave"
active = True
want_address = []
while active:
    address = input(question)
    if address == 'quit':
        break
    else:
        want_address.append(address)
print(want_address)