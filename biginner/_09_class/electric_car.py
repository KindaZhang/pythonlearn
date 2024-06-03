#####主讲继承
# from car import Car
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 属性设置默认值
        
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        """通过方法修改属性值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        """通过方法对属性值递增"""
        self.odometer_reading+= miles
    def fill_gas_tank(self):
        pass
        
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately "+str(range)
        message+= " miles on a full charge."
        print(message)
#继承     
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    #   self.battery_size = 70
        self.battery= Battery()
"""
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
""" 
"""
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
"""  

















#类的继承：a继承b，a获取b的全部属性及方法，b称为父类，a称为子类。子类除了父类的属性和方法外可以定义自己的属性和方法
#继承时，父类必须在当前文件里，且位于子类前面
#子类定义时，必须在括号内指定父类的名称，__init__()方法接受创建Car实例所需的信息
#super()函数，将父类和子类关联起来。因为此，父类也称为超类
#重写父类方法，子类中的方法与父类同名，只会关注子类的方法



