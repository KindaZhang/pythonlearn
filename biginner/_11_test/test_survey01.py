import unittest

from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
unittest.main()

#setUp()创建一个调查对象，创建一个答案列表
#setUp()创建一系列实例且设置她们的属性，就可以在测试方法中使用这些实例
#测试用例，完成衣蛾单元测试，打印一个字符，测试通过打印句点，测试引发错误打印一个E，测试断言打印一个F