class Person:

    name:str = "default"
    gender:str ="default"
    age:int = 20
    money:float = 1000

    def __init__(self,name,gender,age,money):
        self.name = name
        self.gender =gender
        self.age = age
        self.money =money

    def set_name(self,name):
        self.name = name
    def eat(self):
        print("is eating")

    def sleep(self):
        print("is sleeping")

    def run(self):
        print("is sleeping")
    @classmethod
    def classmethod(cls):
        pass
    @staticmethod
    def make_monney:
        paprint("can make money")

    p = Person(1,2,2,3)
    print(p.name)
    Person.run()
'''
1.声明类方法，类和实例可以调用
@classmethod
    def classmethod(cls):
        pass
2.定义静态方法@staticmethod
    @staticmethod
    def make_monney:
        PASS

'''