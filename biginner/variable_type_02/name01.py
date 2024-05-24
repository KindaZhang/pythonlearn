#############
#这是2-2小节的文中代码
#############
##
#
## 运用函数title()upper()lower()以及字符串拼接
#
##

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#title()单词首字母大写
#upper()全部单词大写
#lower()全部单词小写


first_name = "ada"
last_name = "lovelace"
full_name = first_name+" "+last_name
print(full_name)
print("Hello,"+full_name.title()+"!")
message = "Hello,"+full_name.title()+"!"
print(message)

#字符串合并用 + ----拼接
#拼接没有自动加空格，需自己加