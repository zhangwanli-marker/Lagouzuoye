#创建 自行车类
class Buycle:
    def run(self):
        print(f"骑行的里程数为：{km}")

#创建 电动车类
class EBuycle(Buycle):
    def __init__(self,battery_level):
        self.batterry_leve = battery_level

    def fill_charge(self):

