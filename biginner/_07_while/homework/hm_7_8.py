#############
#这是7-3小节的课后作业第1题
#############
"""
熟食店：
创建一个名为sandwich_orders的列表，
在其中包含各种三明治的名字；
再创建一个名为finished_sandwiches的空列表。
遍历列表sandwich_orders，
对于其中的每种三明治，
都打印一条消息，
如I made your tuna sandwich，
并将其移到列表finished_sandwiches。
所有三明治都制作好后，
打印一条消息，将这些三明治列出来。
"""
##
#
## while处理列表
#
##
sandwich_orders =['牛肉三明治','煎蛋三明治','猪肉三明治']
finished_sandwiches = []
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("我做了你点的"+sandwich_order)
    finished_sandwiches.append(sandwich_order)
print(finished_sandwiches)