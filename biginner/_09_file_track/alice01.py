#FileNotFoundError
filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\pg73766.txt'
try:
    with open(filename,encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry,the file "+filename+" does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file "+filename+" has about "+str(num_words)+" words.")

#split()函数，以空格为分隔符，查分文本，存储在列表内，计算多少单词