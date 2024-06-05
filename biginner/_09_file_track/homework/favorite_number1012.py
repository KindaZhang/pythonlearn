import json

def get_stored_num():
    try:
        filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\homework\favorite_number.json'

        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number
def get_new_num():
    filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\homework\favorite_number.json'
    number = input("请输入喜欢的数字：")
    with open(filename,'w') as f_obj:
        json.dump(number,f_obj)
    return number
        
def favorite_number():
    number = get_stored_num()
    if number:
        print("用户喜欢的数字是："+number)
    else:
        print("已经输入用户喜欢的数字!")
        
favorite_number()