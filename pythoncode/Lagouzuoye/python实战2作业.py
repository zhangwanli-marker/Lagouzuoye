import yaml


# 创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
class Animal:
    def __init__(self, name, color, age, gender):
        self.name: str = name
        self.color: str = color
        self.age: int = age
        self.gender: str = gender

    def canshout(self):
        print("我会叫")

    def canrun(self):
        print("我会跑")


# 创建子类【猫】，继承【动物类】
class Cat(Animal):
    # - 复写父类的__init__方法，继承父类的属性，
    # def __init__(self, name="coco", color="黄色", age=2, gender="female", hair="短毛"):
    #     self.name: str = name
    #     self.color: str = color
    #     self.age: int = age
    #     self.gender: str = gender
    #     self.hair: str = hair
    # - 复写父类的__init__方法，继承父类的属性，
    def __init__(self, name, color, age, gender, hair="短毛"):

        super().__init__(name,color,age,gender)
    #     super(Cat, self).__init__(name, color, age, gender)
        # 添加一个新的属性，毛发=短毛，
        self.hair = hair

    def catchmouse(self):
        print(f"{self.name, self.color, self.age, self.gender, self.hair}捉到老鼠了")

    def canshout(self):
        print("喵喵叫")


class Dog(Animal):
    # - 复写父类的__init__方法，继承父类的属性，
    def __init__(self, name, color, age, gender, hair="长毛"):
        super().__init__(name, color, age, gender)
        # super(Dog, self).__init__(name, color, age, gender)
        # 添加一个新的属性，毛发=长毛，
        self.hair = hair

    def doorkeeper(self):
        print(f"{self.name, self.color, self.age, self.gender, self.hair}")

    def canshout(self):
        print("汪汪叫")


with open("animal.yaml", 'rb') as f:
    datas = yaml.safe_load(f)
    catdatas = datas[0]["cat"]
    dogdatas = datas[1]["dog"]
    print(datas)

    cat = Cat(name=catdatas["name"], color=catdatas["color"], age=catdatas["age"], gender=catdatas["gender"])
    cat.catchmouse()
    dog = Dog(name=dogdatas["name"], color=dogdatas["color"], age=dogdatas["age"], gender=dogdatas["gender"])
    dog.doorkeeper()
