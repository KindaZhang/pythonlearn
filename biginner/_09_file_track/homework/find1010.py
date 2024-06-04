filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\pg73766.txt'
try:
    with open(filename,encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry,the file "+filename+" does not exist."
    print(msg)
else:
    num_words1 = contents.count('the')
    num_words2 = contents.lower().count('the')
    print("The file "+filename+" has about "+str(num_words1)+" words.")
    print("The file(lower) "+filename+" has about "+str(num_words2)+" words.")
