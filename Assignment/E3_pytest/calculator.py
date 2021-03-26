# 定义计算器🧮
import decimal


class Calculator:
    # 定义加法
    def add(self, a, b):
        if isinstance(a, float) or isinstance(b, float):
            c = decimal.Decimal(str(a)) + decimal.Decimal(str(b))
            c = float(c)
        else:
            c = a + b
        return c

    # 定义减法
    def sub(self, a, b):
        if isinstance(a, float) or isinstance(b, float):
            c = decimal.Decimal(str(a)) - decimal.Decimal(str(b))
            c = float(c)
        else:
            c = a - b
        return c

    # 定义乘法
    def multiplication(self, a, b):
        c = a * b
        return c

    # 定义除法
    def division(self, a, b):
        if b == 0:
            c = '除数不能为0'
            print(c)
        else:
            c = a / b
        return c
