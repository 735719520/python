print('你好，请输入您的名字：')
name = input()
print('hello,',name)
print('我们来玩儿个小游戏')
print('在你的脑海里想一个10以内的整数我来猜出它')
print('请问您输入的数字是偶数吗？')
print('请输入yes or no')
x = input()
if x == 'yes':
    print('您想的数字吉利吗？')
    print('请输入yes or no')
    y = input()
    if y == 'yes':
            print('您所想的数字谐音是辈分的称呼吗？')
            print('请输入yes or no')
            z = input()
            if z == 'yes':
                print('您所想的数字是8')
            else:
                print('您所想的数字是6')
    else:
        print('您所想的数字谐音与死亡有关吗？')
        print('请输入yes or no')
        q = input()
        if q == 'yes':
            print('您所想的数字是4')
        else:
            print('您所想的数字是2')
else:
    print('您所想的数字能被3整除吗?')
    print('请输入yes or no')
    w = input()
    if w == 'yes':
        print('您想的数字谐音是辈分的称呼吗？')
        print('请输入yes or no')
        i = input()
        if x == 'yes':
            print('您所想的数字是9')
        else:
            print('您所想的数字是3')
    else:
        print('您所想的数字的平方等于自身吗？')
        print('请输入yes or no')
        r = input()
        if r == 'yes':
            print('您所想的数字是1')
        else:
            print('您所想的数字是5')