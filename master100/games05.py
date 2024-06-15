from random import randint
#CRAPS赌博游戏 本钱：1000
money = 1000
while money > 0:   #持续进行知道无本钱
    
    print('你得总资产为：',money) #每次运行后查看本钱
    needs_go_on = False          #控制其他点数是否玩的状态
    while True:                  #确保下注金额，循环是保证真的下注
        debt = int(input('请下注：')) 
        if 0 < debt <= money:
            break
    first = randint(1,6) +randint(1,6) #第一次掷色子，我本来想的是如何两次如何掷色子，因为，分开来就不好继续进行
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11: #第一次玩家胜利
        print('玩家胜！')
        money += debt              #赌钱增加押注
    elif first == 2 or first == 3 or first == 12:#庄家胜
        print('庄家胜！')
        money -= debt#玩家本钱减少
    else:
        needs_go_on = True
    while needs_go_on:  #其他点数继续玩
        needs_go_on = False
        current = randint(1,6)+randint(1,6)
        print('玩家摇出了%d点'% current)
        if current == 7:
            print('庄家胜！')
            money -= debt
        elif current == first:
            print('玩家胜！')
            money += debt
        else:
            needs_go_on = True
print('你破产了，游戏结束！')