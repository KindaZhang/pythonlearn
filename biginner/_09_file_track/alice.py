#FileNotFoundError
filename = r'E:\git_code\pythonlearn\biginner\_09_file_track\alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry,the file "+filename+" does not exist."
    print(msg)
    