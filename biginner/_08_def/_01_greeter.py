#############
#这是单元8的文中代码
#############
##
#
## 函数
#
##

#定义函数

def greet_user():
    print("Hello!")
greet_user()

#带参数的函数
def greet_user(username):
    print("Hello!"+username.title()+"!")
greet_user('jesse')



##########传递实参###########

#位置实参 pets.py
def describe_pet(pet_name,animal_type='dog'):
    """这里显示的是函数的功能的注释，很重要"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster','harry')
describe_pet('dog','willie')
describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')


##########返回值###########

#formatted_name.py

def get_formatted_name(first_name,last_name):
    full_name = first_name+' '+last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)



#可选实参

def get_formatted_name(first_name,middle_name,last_name):
    full_name = first_name+' '+middle_name+' '+last_name
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)


def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)


#返回字典 person.py
def build_person(first_name,last_name):
    person = {'first':first_name,'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)


def build_person(first_name,last_name,age=''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix',age=27)
print(musician)

#while 循环 greeter.py
"""
def get_formatted_name(first_name,last_name):
    full_name = first_name+' '+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name:")
    l_name = input("Last name:")
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, "+formatted_name+"!")

"""

def get_formatted_name(first_name,last_name):
    full_name = first_name+' '+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name =='q':
        break
    l_name = input("Last name:")
    if l_name =='q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, "+formatted_name+"!")

##########传递列表###########

#greet_user.py
def greet_users(names):
    for name in names:
        msg = "Hello,"+name.title()+"!"
        print(msg)
usernames = ['hannah','ty','margot']
greet_users(usernames)


#在函数在修改列表 printing_models.py
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
while  unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model:"+current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    
    
def print_models(unprinted_designs,completed_models):
    while  unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model:"+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#切片 禁止修改列表元素




##########传递任意数量的实参###########

#pizza.py
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')


#结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)
    print(toppings)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#使用任意数量的关键字实参 user_profile.py
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_person('albert','einstein',location='princeton',field='physics')
print(user_profile)






#定义函数 def 函数名：
#             function
#def 就是告诉电脑，我要创建一个函数
#实参和形参 
#位置实参和关键字实参。 位置实参：顺序需要和形参的顺序相同,默认自动匹配 
# 关键字实参：在函数调用时加上形参，直接指定赋值。由变量名和值组成，可以使用列表和字典
#关键字实参的顺序没什么关系
#默认值 函数定义时直接赋值,需要放在函数末尾，因为别的实参会被认为是位置实参，关联到第一个形参
#可选形参就是给一个空字符串的默认值 python中空字符串解读为true
#创建空元组 -- *变量名，就是将所有的值封装在元组内
#创建空字典 -- **变量名