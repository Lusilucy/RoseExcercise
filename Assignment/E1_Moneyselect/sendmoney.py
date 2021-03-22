def send_money():
    month_money = int(input('请输入个人月工资金额：'))
    money = []
    for i in range(0, 13):
        money.append(i * month_money)
        i += 1
    print('有小钱钱啦，好开心呀～！❤️')
    return money

