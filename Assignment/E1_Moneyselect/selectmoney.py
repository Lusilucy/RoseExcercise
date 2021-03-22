import savemoney
import sendmoney
def select_money():
    month = int(input('请输入查询工资卡余额的月份：'))
    if month in range(0,13):
        print('%s月工资卡余额为：%s' % (month, savemoney.save_money + sendmoney.send_money()[month]))
    else:
        print('输入月份有误，请输入输入数字0-12,0代表查询工资卡初始余额')




if __name__ == '__main__':
    select_money()
    print(savemoney.save_money)
    print(__name__)