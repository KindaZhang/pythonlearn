class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        print(self.name.title()+" rolled over!")
        
my_dog = Dog('willie',6)
your_dog = Dog('lucy',3)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
my_dog.roll_over()
print("\nYour dog's name is "+my_dog.name.title()+".")
print("Your dog is "+str(my_dog.age)+" years old.")
your_dog.sit()
        
#首字母大写的名称是类，从空白创建类括号内不添加
#_init_()--方法，包含形参，其中self必不可少,未显式包含return，但自动返回一个实例
#且位于其他形参前面，此方法是必不可少的，内含多少元素，那么实例化的时候就要提供多少值
#可以通过实例访问的变量称为属性
#