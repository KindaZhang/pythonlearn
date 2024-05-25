#############
#这是5-4小节的课后作业第3题
#############
"""
检查用户名：
按下面的说明编写一个程序，
模拟网站确保每位用户的用户名都独一无二的方式。
·创建一个至少包含5个用户名的列表，并将其命名为current_users。
·再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users中。
·遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
·确保比较时不区分大小写；换句话说，如果用户名'John'已被使用，应拒绝用户名'JOHN'。
"""
##
#
## if-else语句
#
##

current_users = ['Admin','user001','user002','user003','visitor']

new_users = ['admin','visitor001','visitor002','visitor003','User001']
users = []
for current_user in current_users:
    users.append(current_user.lower())
for new_user in new_users:
    if new_user.lower() in users:
        print(new_user.title()+" is used!")
    else:
        print(new_user.title()+" is not used.")
