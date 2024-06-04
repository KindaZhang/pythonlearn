def open_filename(filename):
    try:
        with open(filename,encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileExistsError:
        print("文件不存在！")
    else:
        print("宠物的名字是：\n"+contents)
filenames = [r'E:\git_code\pythonlearn\biginner\_09_file_track\homework\cats.txt',r'E:\git_code\pythonlearn\biginner\_09_file_track\homework\dogs.txt','pigs.txt']

for filename in filenames:
    open_filename(filename)