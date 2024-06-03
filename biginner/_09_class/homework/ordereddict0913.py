
from collections import OrderedDict as words
words = {
    'list()':'生成列表',
    'str()':'强制转换数据类型为字符串',
    'sorted()':'临时排序',
    'range()':'生成数字',
    'len()':'数据长度',
    }
words['sort()'] = '永久排序'
words['int()'] = '强制转换数据类型为整型'
words['set()'] = '去重且创建一个合集'
words['items()'] = '返回键值对列表'
words['keys()'] = '返回键列表'
for key,value in words.items():
    print(key+":")
    print(value)