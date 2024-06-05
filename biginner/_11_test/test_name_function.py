import unittest

from name_function import get_formatted_name
class NameTestCase(unittest.TestCase):
    def  test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
unittest.main()




#导入模块unittest 创建继承unittest.TestCase 的类，对需要进行测试的方法进行测试
#unittest最有用的是断言方法
#6种断言方式
