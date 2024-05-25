#############
#这是5-3小节的课后作业第4题
#############
"""
人生的不同阶段：
设置变量age的值，再编写一个if-elif-else结构，根据age的值判断处于人生的哪个阶段。
·如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
·如果一个人的年龄为2（含）～4岁，就打印一条消息，指出他正蹒跚学步。
·如果一个人的年龄为4（含）～13岁，就打印一条消息，指出他是儿童。
·如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。
·如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。
·如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人。
"""
##
#
## if_elif-else语句
#
##

age = 55
if age <2:
    print("She is a baby.Her age is behind two years old.")
elif age >=2 and age <4:
    print("She is learning walking.Her age is between two years old and four years old.")
elif age >=4 and age <13:
    print("She is a child.Her age is between four years old and thirteen years old.")
elif age >=13 and age <20:
    print("She is a teenager.Her age is between thirteen years old and twenty years old.")
elif age >=20 and age <65:
    print("She is a adult.Her age is between twenty years old and sixty-five years old.")
else:
     print("She is the elderly.Her age is more sixty-five years old.")