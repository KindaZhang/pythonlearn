#############
#这是6-4小节的课后作业第3题
#############
"""
 喜欢的地方：
 创建一个名为favorite_places的字典。
 在这个字典中，
 将三个人的名字用作键；
 对于其中的每个人，
 都存储他喜欢的1～3个地方。
 为让这个练习更有趣些，
 可让一些朋友指出他们喜欢的几个地方。
 遍历这个字典，
 并将其中每个人的名字及其喜欢的地方打印出来。
"""
##
#
## 字典嵌套列表
#
##
favorite_places = {
    '张三':['上海','北京'],
    '李四':['太原','西安','海南'],
    '王五':['杭州'],
}
for name,favorite_place in favorite_places.items():
    print("朋友名称：")
    print(name)
    print("她喜欢的城市：")
    for place in favorite_place:
        print(place)
