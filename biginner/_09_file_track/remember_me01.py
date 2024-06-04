import json

filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back,"+username+"!")
else:
    print("Welcome back,"+username+"!")