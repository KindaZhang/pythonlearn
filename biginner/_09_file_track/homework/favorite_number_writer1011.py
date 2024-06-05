import json
filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\homework\favorite_number.json'
number = input("请输入喜欢的数字：")
with open(filename,'w') as f_obj:
   json.dump(number,f_obj)