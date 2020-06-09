class Person:
    name: str = "default"
    gender: str = "default"
    age: int = 10
    __money: float = 10000

    def __init__(self, name, gender, age, money):
        self.name = name
        self.gender = gender
        self.age = age
        # 定义私有属性__money
        self.__money = money

    def eat(self):
        print(f"{self.name} is eating")

    def getmoney(self):
        print("获取私有属性money")
        return self.__money

    def sleep(self):
        print(f"{self.name} is sleep")

    def run(self):
        print(f"{self.name} is running")

    # 定义私有方法
    def __makemoney(self):
        print(f"{self.name} can make money")

    @classmethod
    def classmethod(cls):
        print("这是一个类方法")

    @staticmethod
    def writecode():
        print("这是一个静态方法")


class Funnyman(Person):
    def fun(self):
        print(f"{self.name} is funny")
    #类中的方法不可以没有self
    def qq(q):
        pass

class Singerman(Person):
    def makemoney(self, moneynum="10w"):
        print(f"{self.name} can make {moneynum}")


funnyman = Funnyman("st", "男", 30, 10000)
funnyman.eat()
funnyman.qq()
# 查看实例有哪些可调用的方法
print(dir(funnyman))

# 调用私有方法
funnyman._Person__makemoney()

Person.classmethod()
Person.writecode()

p = Person("st", "男", 30, 10000)
p.classmethod()
p.writecode()

singerman = Singerman("st", "男", 30, 10000)
singerman.makemoney()
#定义类方法后，类本身和实例都可以调用
singerman.writecode()
print(dir(singerman.makemoney()))
