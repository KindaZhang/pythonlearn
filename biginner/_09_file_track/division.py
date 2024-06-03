#ZeroDivisionError异常
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#异常
print("Give me two numbers,and I'll divide them.")
print("Enter'q' to qiut.")
while True:
    first_number = input("\nFirst number:")
    
    if first_number == 'q':
        break
    second_number = input("Second number:")
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can;t divide by 0!")
    else:
        print(answer)
        
#try-except-else,执行顺序，try内部房这的是可能引起一场的代码，except后添加一场名称，如果遇到这个一场，执行except中的代码。如果try执行无异常，则执行else中的代码。