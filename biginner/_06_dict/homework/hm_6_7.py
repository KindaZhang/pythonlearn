#############
#这是6-4小节的课后作业第1题
#############
"""
人：
在为完成练习6-1而编写的程序中，
再创建两个表示人的字典，
然后将这三个字典都存储在一个名为people的列表中。
遍历这个列表，将其中每个人的所有信息都打印出来
"""
##
#
## 字典列表
#
##

people1 = {'first_name':'san','last_name':'zhang','age':23,'city':'bei jing'}
people2 = {'first_name':'wu','last_name':'wang','age':13,'city':'shang hai'}
people3 = {'first_name':'san','last_name':'li','age':29,'city':'tai yuan'}
people =[people1,people2,people3]
for person in people:
    print("人详细信息：")
    print(person['first_name']+" "+person['last_name'])
    print(person['age'])
    print(person['city'])