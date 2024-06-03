message = input("请输入你的姓名：")
filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\homework\guest.txt'
with open(filename,'w') as f_object:
    f_object.write(message)