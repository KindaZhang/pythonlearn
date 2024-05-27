#############
#这是6-3小节的课后作业第2题
#############
"""
河流：
创建一个字典，在其中存储三条大河流及其流经的国家。
其中一个键—值对可能是'nile':'egypt'。
·使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
·使用循环将该字典中每条河流的名字都打印出来。
·使用循环将该字典包含的每个国家的名字都打印出来。
"""
##
#
## items() keys()values()
#
##

rivers ={'nile':'egypt','Amazon River':'bazil','Mississippi River':'america'}
for key,value in rivers.items():
    print("The "+key.title()+" run through "+value.title())
print("河流名称：")
for key in rivers.keys():
    print(key.title())
print("河流经过的国家名称：")
for value in rivers.values():
    print(value.title())
    