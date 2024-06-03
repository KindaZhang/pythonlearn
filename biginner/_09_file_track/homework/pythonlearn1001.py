filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\homework\learning_python.txt'
with open(filename) as f_object:
    contents = f_object.read()
    print(contents.rstrip())

with open(filename) as f_object:
    for line in f_object:
        print(line.rstrip())
    
with open(filename) as f_object:
    lines = f_object.readlines()
    for line in lines:
        print(line.rstrip())
    