filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\homework\learning_python.txt'
with open(filename) as f_object:
    lines = f_object.readlines()
p_string = ''
for line in lines:
    line = line.replace('Python', 'C')
    p_string+= line
print(p_string)
    