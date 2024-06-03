filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\homework\visitor.txt'
with open(filename,'w') as f_object:
    while True:
        message = input("请输入你的名字：")
        
        if message == 'q':
            break
        else:
            print("欢迎！！！")
            print("（输入q退出）")
            f_object.write(message+'\n')
        

    