import json
filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\homework\favorite_number.json'
try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    pass
else:
    print(number)