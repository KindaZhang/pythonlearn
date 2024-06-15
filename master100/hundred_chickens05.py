
#百鸡问题

for x in range(0, 100):
    for y in range(0, 103):
        for z in range(0, 100):
            if 5 * x + 3 * y + z/3 == 100 and x + y + z == 100:
                print("公鸡数量："+str(x)+" 母鸡数量："+str(y)+" 小鸡数量："+str(z))


"""
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
            """