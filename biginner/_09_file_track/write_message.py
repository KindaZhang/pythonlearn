filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

#a
filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")



#r--只读，w--写入，a--附加模式，r+--读取和写入
#文件不存在自动创建，文件存在，则写入时，回清空该文件
#write() 将一串字符串写入文件
#若是其他类型，需要进行类型转换，转换成字符串类型