#############
#这是8-5小节的课后作业第2题
#############
"""
用户简介：
复制前面的程序user_profile.py，
在其中调用build_profile()来创建有关你的简介；
调用这个函数时，
指定你的名和姓，
以及三个描述你的键-值对。
"""
##
#
## 
#
## 

def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('张','三',hobby='摄影',loaction='江苏',wanted='成为一名极客')
print(user_profile)