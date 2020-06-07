class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hungry = True
        print("鱼的初始化位置为：%s,%s" % (self.x, self.y))

    def move(self):
        self.x -= 1
        self.y -= 1
        print("鱼现在的位置为(%s,%s)" % (self.x, self.y))


class Goldfish(Fish):
    def eat(self):

        if self.hungry:
            print("我好饿，我要吃东西*><*")
        else:
            print("吃饱了，好开心><")


