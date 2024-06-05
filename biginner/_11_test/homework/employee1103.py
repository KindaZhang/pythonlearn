class Employee():
    def __init__(self,firstname,lastname,salary):
      self.name = firstname.title()+' '+lastname.title()
      self.salary = salary
    def give_raise(self,add_raise=5000):
        self.salary+= add_raise
    def print_info(self):
        print(self.name.title())
        print(self.salary)
          