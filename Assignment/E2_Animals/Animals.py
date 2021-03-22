'''
课后作业
1、自己写一个面向对象的例子：
- 比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
    - 创建子类【猫】，继承【动物类】，
    - 复写父类的__init__方法，继承父类的属性，
    - 添加一个新的属性，毛发=短毛，
    - 添加一个新的方法， 会捉老鼠，
    - 复写父类的‘【会叫】的方法，改成【喵喵叫】

- 创建子类【狗】，继承【动物类】，
    - 复写父类的__init__方法，继承父类的属性，
    - 添加一个新的属性，毛发=长毛，
    - 添加一个新的方法， 会看家，
    - 复写父类的【会叫】的方法，改成【汪汪叫】

- 调用 name== ‘main’：
    - 创建一个猫猫实例
        - 调用捉老鼠的方法
        - 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
    - 创建一个狗狗实例
        - 调用【会看家】的方法
        - 打印【狗狗的姓名，颜色，年龄，性别，毛发】。

2、使用yaml 来管理猫猫，狗狗的属性
'''

class Animal():
    def __init__(self,name,color,age,sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        self.calls = 'calls'

    def voice(self):
        print(f'{self.name} can {self.calls}!')

    def run(self):
        print(f'{self.name} can run!')

class Cat(Animal):
    def __init__(self,name,color,age,sex):
        super(Cat,self).__init__(name,color,age,sex)
        self.hair = 'short hair'

    def catch_mouse(self):
        print(f'{self.name} can catch mice!')
        return f'{self.name} can catch mice!'

    def voice(self):
        self.calls = 'meow'
        super(Cat, self).voice()


class Dog(Animal):
    def __init__(self,name,color,age,sex):
        super(Dog, self).__init__(name,color,age,sex)
        self.hair = 'long hair'

    def lookafter_house(self):
        print(f'{self.name} can look after the house!')

    def voice(self):
        self.calls = 'bark'
        super(Dog, self).voice()



if __name__ == '__main__':
    # cat1 = Cat('WuHuang','White and Black',3,'famale')
    # cat1.catch_mouse()
    # cat1.voice()
    # print(f'猫猫名字：{cat1.name},猫猫颜色：{cat1.color},猫猫年龄：{cat1.age},猫猫性别：{cat1.sex},猫猫毛发：{cat1.hair},猫猫技能：{cat1.catch_mouse()}')
    #
    # dog1 = Dog('BaZHei','Brown','5','male')
    # dog1.lookafter_house()
    # dog1.voice()
    # print(f'{dog1.name},{dog1.color},{dog1.age},{dog1.sex},{dog1.hair}')


    # c1 ={'name':'WuHuang','color':'White and Black','age':3,'sex':'famale'}
    import yaml
    with open('data_animals.yaml') as f:
        data_animals = []
        for i in yaml.safe_load_all(f):
            # print(i)
            default = i['default']
            data_animals.append(default)
        # print(data_animals)
        # print(data_animals[0])


    d_cat = data_animals[0]
    d_dog = data_animals[1]

    cat = Cat(d_cat['name'],d_cat['color'],d_cat['age'],d_cat['sex'])
    cat.catch_mouse()
    cat.voice()
    print(f'猫猫名字：{cat.name},猫猫颜色：{cat.color},猫猫年龄：{cat.age},猫猫性别：{cat.sex},猫猫毛发：{cat.hair},猫猫技能：{cat.catch_mouse()}')


    dog1 = Dog(d_dog['name'],d_dog['color'],d_dog['age'],d_dog['sex'])
    dog1.lookafter_house()
    dog1.voice()
    print(f'{dog1.name},{dog1.color},{dog1.age},{dog1.sex},{dog1.hair}')