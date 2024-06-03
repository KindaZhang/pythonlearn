filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\homework\request.txt'
with open(filename,'w') as f_object:
    while True:
        message = input("为什么喜欢编程？")
        
        if message == 'q':
            break
        else:
            print("（输入q退出）")
            f_object.write(message+'\n')
        