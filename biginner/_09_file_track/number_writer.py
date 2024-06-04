import json
numbers = [2,3,5,7,11,18]
filename =  r'E:\git_code\pythonlearn\biginner\_09_file_track\number_writer.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)




















#模块json json.dump()--接受两个实参，要存储的数据和用来存储的文件对象json.load()参数是存储数据的文件