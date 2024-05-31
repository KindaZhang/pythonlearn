#############
#这是8-3小节的课后作业第1题
#############
"""
城市名：
编写一个名为city_country()的函数，
它接受城市的名称及其所属的国家。
这个函数应返回一个格式类似于下面这样的字符串：
"Santiago,Chile"
至少使用三个城市-国家对调用这个函数，
并打印它返回的值。
"""
##
#
## return 
#
##
def city_country(city,country):
    knowledge = city.title()+","+country.title()
    return knowledge
konwledge = city_country('santiago','chile')
print(konwledge)
konwledge = city_country('xi an','china')
print(konwledge)
konwledge = city_country('new york','america')
print(konwledge)