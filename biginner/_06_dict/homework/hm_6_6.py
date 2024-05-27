#############
#这是6-3小节的课后作业第3题
#############
"""
调查：
在6.3.1节编写的程序favorite_languages.py中执行以下操作。
·创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
·遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。。
"""
##
#
## 字典
#
##


favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
researchers = ['jen','li','phil','wang']
for name in favorite_languages.keys():
    if name not in researchers:
        print(name.title()+"请接受调查")
    else:
        print("感谢你的配合,"+name.title())
