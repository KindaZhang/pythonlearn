for i in range(2,101):
    needs_go_on = True
    for x in range(2,i+1):
        if i % x == 0 and i != x:
            needs_go_on = False
            break
    if needs_go_on:
        print('%d是素数' % i)