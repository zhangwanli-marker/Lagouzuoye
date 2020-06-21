
# - 添加一个新的属性，毛发=短毛，
# - 添加一个新的方法， 会捉老鼠，
# - 复写父类的‘【会叫】的方法，改成【喵喵叫】
# 创建子类【狗】，继承【动物类】，
# - 复写父类的__init__方法，继承父类的属性，
# - 添加一个新的属性，毛发=长毛，
# - 添加一个新的方法， 会看家，
# - 复写父类的【会叫】的方法，改成【汪汪叫】
# 创建一个猫猫实例
# - 调用捉老鼠的方法
# - 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
# 创建一个狗狗实例
# - 调用【会看家】的方法
# - 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
# 4、使用 yaml 来管理实例的属性
import yaml
class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def canshout(self):
        pass

    def canrun(self):
        pass


class Cat(Animal):

    def __init__(self, name, color, age, gender, hair="短毛"):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.hair = hair

    def catchmouse(self):
        print(f"{self.name, self.color, self.age, self.gender, self.hair},捉到了老鼠")

    def canshout(self):
        print ("猫咪咪咪叫")


class Dog(Animal):
    def __init__(self, name, color, age, gender, hair="长毛"):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.hair = hair

    def guarddoor(self):
        print(f"{self.name, self.color, self.age, self.gender, self.hair}")

    def canshout(self):
        print("小狗汪汪叫")

with open(r'E:/测试开发学习/git/Pythoncode/Lagouzuoye1/pythoncode/mydata.yml',encoding='UTF-8')  as f:
    data = yaml.safe_load(f)
    print (data)

    cat = Cat(data)

