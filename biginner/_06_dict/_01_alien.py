#############
#这是单元6的文中代码
#############
##
#
## 字典
#
##


#初识字典 alien.py
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])


alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print("You just earned "+str(new_points)+" points!")


#添加键值对
alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#空字典

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


#修改字典的值
alien_0 = {'color':'green'}
print("The alien is "+alien_0['color']+".")
alien_0['color'] = 'yellow'
print("The alien is now "+alien_0['color']+".")



alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position:"+str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position']+x_increment
print("New x-position:"+str(alien_0['x_position']))


#删除键值对
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)


#类似对象组成的字典
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',  #,可以添加也可以不添加
}
print("Sarah's favorite language is "+favorite_languages['sarah'].title()+".")

#遍历字典

#遍历键值对  user.py
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key,value in user_0.items():
    print("\nKey:"+key)
    print("Value:"+value)

#favorite_language.py
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite_language is "+language.title()+".")

#遍历所有键
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name in favorite_languages.keys():
    print(name.title())

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("  Hi "+name.title()+",I see your favorite language is "+favorite_languages[name].title()+"!")

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
if 'erin' not in favorite_languages.keys():
    print("Erin,please take our poll!")

#排序
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title()+",thank you for taking the poll.")

#遍历值
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.keys():
    print(language.title())


#去除重复
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.keys()):
    print(language.title())

###嵌套 字典嵌套列表，列表嵌套字典

#字典列表 aliens.py
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
 
#初级
aliens = []   
for alien_number in range(30):
    new_alien =  {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)  
print("...")
print("Total number of aliens:"+str(len(aliens)))

#中级
aliens = []   
for alien_number in range(30):
    new_alien =  {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'meidum'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[0:5]:
    print(alien)
print("...")


#字典中存储列表 pizza.py
pizza = {
    'crust':'trick',
    'toppings':['mushrooms','extra cheese']
}
print("You ordered a "+pizza['crust']+"-crust pizza "+"with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)


#favorite_languages.py
favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}
for name,languages in favorite_languages.items():
    print("\n"+name.title()+"'s favorite languages are:")
    for language in languages:
        print("\t"+language.title())

##字典存储字典

#many_users.py
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username,user_info in users.items():
    print("\nUsername:"+username)
    full_name = user_info['first']+" "+user_info['last']
    location = user_info['location']
    print("\nFull name:"+full_name.title())
    print("\tLocation:"+location.title())








#字典是键-值对,动态结构
#键值对排列顺序和添加顺序不同，python不关心添加顺序，只关心键值对的关联关系
#删除键值对用del 和列表一样 永久删除
#items()函数返回键-值对列表
#keys()函数返回所有键--列表
#values()函数返回所有值--列表
#set()去除重复的元素，且将去重后的元素创建一个集合
#列表和字典的嵌套层级不要太多，太多了可能会有更简单的解决方法
#字典嵌套时，嵌套的字典结构应当相同，否则for循环会很复杂