#重构就是在代码可以正确运行时，将代码划分为函数

import json
def get_stored_username():
    filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\homework\username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("What is your name?")
    filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\homework\username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username
def greet_user():
    username = get_stored_username()
    while True:
        print(username)
        ask = input("用户名是否正确（输入y代表 yes、输入n表示no）")
        if ask == 'y':
            print("Welcome back,"+username+"!")
            break
        else:
            username = get_new_username()
            print("We'll remember you when you come back,"+username+"!")
            
                
    
greet_user()