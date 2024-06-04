import json
filename =  r'E:\git_code\pythonlearn\biginner\_09_file_track\number_writer.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
