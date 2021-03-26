'''
作业：
1、补全计算器（加法，除法）的测试用例
2、使用数据驱动完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
坑1:除数为0的情况
坑2: 自己发现
'''
import pytest
import yaml
import calculator

with open('data_cal_add.yaml', encoding='utf-8') as f1:
    data1 = yaml.safe_load(f1)

with open('data_cal_sub.yml', encoding='utf-8') as f2:
    data2 = yaml.safe_load(f2)

with open('data_cal_mul.yml', encoding='utf-8') as f3:
    data3 = yaml.safe_load(f3)

with open('data_cal_div.yml', encoding='utf-8') as f4:
    data4 = yaml.safe_load(f4)


def setup_module():
    print('开始计算')


def teardown_module():
    print('计算结束')


class TestCalculator:
    def setup_class(self):
        print("TestCalculator测试开始")

    def teardown_class(self):
        print("TestCalculator测试结束")

    def setup(self):
        print('案例执行开始')

    def teardown(self):
        print('案例执行结束')

    @pytest.mark.parametrize('a,b,c', data1.values(), ids=data1.keys())
    def test_add(self, a, b, c):
        c1 = calculator.Calculator()
        assert c1.add(a, b) == c

    @pytest.mark.parametrize('a,b,c', data2.values(), ids=data2.keys())
    def test_sub(self, a, b, c):
        c2 = calculator.Calculator()
        assert c2.sub(a, b) == c

    @pytest.mark.parametrize('a,b,c', data3.values(), ids=data3.keys())
    def test_mul(self, a, b, c):
        c3 = calculator.Calculator()
        assert c3.multiplication(a, b) == c

    @pytest.mark.parametrize('a, b, c',data4.values(),ids=data4.keys())
    def test_div(self, a, b, c):
        c4 = calculator.Calculator()
        assert c4.division(a, b) == c
