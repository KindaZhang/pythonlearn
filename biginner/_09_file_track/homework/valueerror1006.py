try:
    num1 = int(input("请输入第一个数字："))
    num2 = int(input("请输入第二个数字："))
except ValueError:
    print("输入都不是数字")
else:
    num = num1 + num2
    print("数字之和为：")
    print(str(num))