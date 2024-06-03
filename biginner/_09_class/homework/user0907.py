class User():
    def __init__(self,first_name,last_name,age):
        self.name = first_name+last_name
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        print("用户姓名："+self.name)
        print("用户年龄："+str(self.age))
    def greet_user(self):
        print("你好呀！！！"+self.name+"!!!")
    def increment_login_attempts(self):
        self.login_attempts+= 1
    def reset_login_attempts(self):
        self.login_attempts = 0
    def print_login_attempts(self):
        print("登录了"+str(self.login_attempts)+"次")

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = ['can add post','can delete post','can ban user']
    def show_privileges(self):
        print("管理员的权限：")
        for privilege in self.privileges:
            print(privilege)

admin001 = Admin('王','五',22)
admin001.show_privileges()