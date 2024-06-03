class Resaurant():
    def __init__(self, restaurant_name,cuisine_type):
      self.name = restaurant_name
      self.ctype = cuisine_type
    def describe_restaurant(self):
        print("餐馆的名字是："+self.name)
        print("餐馆的类型："+self.ctype)
    def open_restaurant(self):
        print("餐馆开门了！")
resaurant1 = Resaurant('热辣滚烫','火锅店')
resaurant1.open_restaurant()
resaurant1.describe_restaurant()