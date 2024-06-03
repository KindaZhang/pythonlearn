#############
#这是单元5的文中代码
#############
##
#
## if语句
#
##

#初识if语句 cars.py

cars = ['ausi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(cars.title())
        
#运算符 == != toppings.py magic_number.py
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    
answer = 17
if answer != 42:
    print("That is not the correct answer.Please try again!")
    

#包含 in  banned_users.py
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(user.title()+",you can post a response if you wish.") 
    
#if语句使用 voting.py
age = 19
if age >= 18:
    print("You are old enough to vote!")


age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")


#if-else语句使用
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
    


#if-elif-else语句
age = 12
if age <4:
    print("Your admission cost is $0.")
elif age <18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
    
    
age = 12
if age <4:
    price = 0
elif age <18:
    price = 5
else:
    price = 10
print("Your admission cost is $"+str(price)+".")


#N个elif
age = 12
if age <4:
    price = 0
elif age <18:
    price = 5
elif age <65:
    price = 10
else:
    price = 5
print("Your admission cost is $"+str(price)+".")
      
      
#省略else
age = 12
if age <4:
    price = 0
elif age <18:
    price = 5
elif age <65:
    price = 10
elif age >=65:
    price = 5
print("Your admission cost is $"+str(price)+".")
    
#测试多个条件  toppings.py
requested_toppings = ['mushroom','extra cheese']
if 'mushroom' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding peppeoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

requested_toppings = ['mushroom','extra cheese']
if 'mushroom' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding peppeoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
    

#查找特殊值 in  toppings.py
requested_toppings = ['mushroom','green peppers','extra cheese']
for requested_toppong in requested_toppings:
    print("Adding "+requested_topping+".")
print("\nFinishef making your pizza!")



requested_toppings = ['mushroom','green peppers','extra cheese']
for requested_toppong in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print("Adding "+requested_topping+".")
print("\nFinishef making your pizza!")


#确保列表不为空
requested_toppings = []
if requested_toppings:
    for requested_toppong in requested_toppings:
        print("Adding "+requested_topping+".")
    print("\nFinishef making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


#多个列表使用
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+".")
    else:
        print("Sorry,we don't have "+requested_topping+".")
print("\nFinished making your pizza!")





#运算符和C语言一致 boolen 也是一样的
#if 语句和C语言差不多 