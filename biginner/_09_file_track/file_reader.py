with open('E:\git_code\pythonlearn\biginner\_09_file_track\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
#逐行读取
filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rfindstrip())

#创建一个包含文件各行内容的列表
filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())











#open()接受的参数，是要打开文件的名称，返回一个表示文件的对象，然后将这个对象存储在后面的变量里
#read()读取文件里面的全部内容，且作为字符串存储在变量里。到达文件末尾时返回一个空字符串，删除用rstrip()
#with 会将不需要访问文件后将其关闭
#文件路径，相对路径和绝对路径
#路径会出现错误，因为\，转义字符，可以在原始字符串前添加r
#print语句也会添加一个换行符
#readlines()函数从文件中读取每一行，且将其存储在列表内

