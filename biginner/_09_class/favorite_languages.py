from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+".")
    
#OrderedDict，可以将字典的添加顺序展现出来
#OrderedDict,创建一个空的有序字典
#类名采用驼峰命名法，每个单词的首字母大写，不采用下划线
#实例名和模块名都采用小写，单词之间加上下划线
#类要添加文档注释，包括功能，模块一样
#类中一个空行，模块中两个空行
#导入，标准库后添加一个空行，然后在编写自己的模块导入语句