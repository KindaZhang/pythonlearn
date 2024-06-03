class User():
    def __init__(self,first_name,last_name,age):
        self.name = first_name+last_name
        self.age = age
    def describe_user(self):
        print("用户姓名："+self.name)
        print("用户年龄："+str(self.age))
    def greet_user(self):
        print("你好呀！！！"+self.name+"!!!")
my_user001 = User('张','三',33)
my_user002 = User('王','二',27)
my_user001.greet_user()
my_user001.describe_user()
my_user002.greet_user()
my_user002.describe_user()