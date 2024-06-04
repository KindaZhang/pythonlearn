#重构就是在代码可以正确运行时，将代码划分为函数

import json
def get_stored_username():
    filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("What is your name?")
    filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username
def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back,"+username+"!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back,"+username+"!")
    
greet_user()