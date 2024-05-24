#############
#这是2-3小节的课后作业第四题
#############
"""
名言2：
重复练习2-5，
但将名人的姓名存储在变量famous_person中，
再创建要显示的消息，
并将其存储在变量message中，
然后打印这条消息。
Albert Einstein once said,“A person who never made a mistake never triedanything new.”
"""
##
#
## +字符串拼接
#
##

famous_person = "albert einstein"
words = '"A person who never made a mistake never tried anything new."'
message = famous_person.title()+" once said,"+words
print(message)