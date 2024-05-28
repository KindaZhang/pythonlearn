#############
#这是单元7的文中代码
#############
##
#
## input()
#
##

#input() parrot.py
message = input("Tell me something,and I will repeat it back to you:")
print(message)


#greeter.py
name = input("Please enter your name:")
print("Hello,"+name+"!")




#geeeter.py
prompt = "If you tell us who you are,we can personalize the messages you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("\nHello,"+name+"!")


#int()q强制转换 rollercoaster.py
height = input("How tall are you ,in inches?")
height = int(height)
if height >=36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're little older.")


#取余 判断是奇数偶数
number = input("Enter a number,and I'll tell you if it's even or odd:")
number = int(number)
if number % 2 ==0:
    print("\nThe number "+str(number)+" is even.")
else:
    print("\nThe number "+str(number)+" is odd.")

#while counting.py
current_number = 1
while current_number <=5:
    print(current_number)
    current_number+=1

#让用户选择退出 parrot.py
prompt = "\nTell me something,and I will repeat it back to you:"
prompt+= "\nEnter 'quit' to end the program."
message  = ""  #指定初始值，使得循环可以进行下去
while message !='quit':
    message = input(prompt)
    if message !='quit':
        print(message)

#使用标志

prompt = "\nTell me something,and I will repeat it back to you:"
prompt+= "\nEnter 'quit' to end the program."
message  = ""  #指定初始值，使得循环可以进行下去
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
        

#break cities.py
prompt = "\nPlease enter the name of a city you have visites:"
prompt+="\n(Enter ' quit'when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!")


#counting.py 
current_number = 0
while current_number <10:
    current_number+=1
    if current_number % 2 == 0:
        continue
    print(current_number)   

#利用while循环在列表间移动元素 confirmed_users.py
unconfirmed_users = ['alice','brian','candance']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user:"+current_user.title())
    confirmed_users.append(current_user)
print("/nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#删除包含特定值的所有列表元素 pets.py

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#用户输入填充字典 mountain_poll.py
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/ no)")
    if repeat =='no':
        polling_active = False
print("\n--- Poll Results ---")
for name,response in responses.items():
    print(name+" would like to climb "+response+".")






#input()等待用户输入
#用户输入解读为字符串 ，可以用int()强制转换类型
#取余%
#while是循环不断，直到不满足指定条件 for循环是针对集合中的诶个元素的一个代码块
#break 跳出循环 continue 跳出此次循环
#避免无限循环，ctrl+C可以跳出无限循环
#for循环不应修改列表