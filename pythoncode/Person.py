class Person:
    def __init__(self,name,gender,age,money):
        self.name:str = "default"
        self.gender:str ="default"
        self.age:int = 20
        self.money:float = 1000

    def set_name(self,name):
        self.name = name
    def eat(self):
        print("is eating")

    def sleep(self):
        pass

    def run(self):
        pass
    @classmethod
    def make_monney:
        pass

    p =Person()
    print(p.name)

    Person.run()

