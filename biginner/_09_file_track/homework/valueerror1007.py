while True:
    try:
        print("输入q退出")
        num1 = int(input("请输入第一个数字："))
        num2 = int(input("请输入第二个数字："))
    except ValueError:
        print("重新输入")
        if num1 == 'q' or num2 == 'q':
            break
        else:
            continue
    else:
        num = num1 + num2
        print("数字之和为：")
        print(str(num))