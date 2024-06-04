def count_words(filename):
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

filenames =[ r'E:\git_code\pythonlearn\biginner\_09_file_track\pg73766.txt',r'E:\git_code\pythonlearn\biginner\_09_file_track\pg73765.txt',r'E:\git_code\pythonlearn\biginner\_09_file_track\pg73767.txt']
for filename in filenames:
    count_words(filename)
    
    
#可以在except语句中使用pass，这样就不会提示什么了，pass也可以充当占位符