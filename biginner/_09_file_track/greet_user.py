import json
filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back,"+username+"!")