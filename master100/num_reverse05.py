num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num *10 + num % 10
    num //= 10
print(reversed_num)

#每次取余，厉害了这种方法
#输入的数字取余，然后赋值给一个默认值为0 的数，由这个数*10 加上num取余值，估值给这个数，然后num整除，也就是num每位数都顺延到下一位数
#我想不到，wuwuwu，加油