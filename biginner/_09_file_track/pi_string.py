filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string+= line.strip()
print(pi_string)
print(len(pi_string))

filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string+= line.strip()
print(pi_string[:52]+"...")
print(len(pi_string))


filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string+= line.strip()
birthday = input("Enter your birthday,in the form mmddyy:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


#读取文本文件时，解读为字符串，需要别的类型，强制转换类型