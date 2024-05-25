#############
#这是5-3小节的课后作业第5题
#############
"""
喜欢的水果：
创建一个列表，其中包含你喜欢的水果，
再编写一系列独立的if语句，检查列表中是否包含特定的水果。
·将该列表命名为favorite_fruits，并在其中包含三种水果。
·编写5条if语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，就打印一条消息，如“You really like bananas!”。
"""
##
#
## if_elif-else语句 in
#
##

favorite_fruits = ['bananas','apple','watermelon']
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'grape' in favorite_fruits:
    print("Grape is not in favorite_fruits!")
if 'coconut' in favorite_fruits:
    print("Coconut is not in favorite_fruits!")
if 'watermelon' in favorite_fruits:
    print("You really like watermelon!")