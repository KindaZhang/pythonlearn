class Resaurant():
    def __init__(self, restaurant_name,cuisine_type):
      self.name = restaurant_name
      self.ctype = cuisine_type
      self.number_served = 0
    def describe_restaurant(self):
        print("餐馆的名字是："+self.name)
        print("餐馆的类型："+self.ctype)
    def open_restaurant(self):
        print("餐馆开门了！")
    def print_number_served(self):
        print("餐馆的就餐人数："+str(self.number_served))
    def set_number_served(self,num):
        self.number_served = num
    def increment_number_served(self,num):
        self.number_served+= num
resaurant1 = Resaurant('热辣滚烫','火锅店')
resaurant1.open_restaurant()
resaurant1.describe_restaurant()
resaurant1.print_number_served()
resaurant1.set_number_served(20)
resaurant1.print_number_served()
resaurant1.increment_number_served(30)
resaurant1.print_number_served()