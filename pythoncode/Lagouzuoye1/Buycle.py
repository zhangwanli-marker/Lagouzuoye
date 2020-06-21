#创建 自行车类
import yaml


class Buycle:
    def run(self,km):
        print(f"骑行的里程数为：{km}")

#创建 电动车类
class EBuycle(Buycle):
    def __init__(self,battery_level):
        self.battery_level = battery_level

    def fill_charge(self,vol):
        print(f"充电：{vol}")
        #目标骑行里程数
    def run(self,km):
        #每骑行10km小号电量1度，加入有10度电，最多电量能骑行 10*10 =100 km
        max_mile =self.battery_level * 10
        leave_mile = km -max_mile
        if leave_mile > 0:
            print(f"已经使用电量骑行了的里程数为：{max_mile}")
            super().run(leave_mile)
        else:
            print(f"电动车行驶了{km}")

if __name__ == '__main__':
    with open('bycle.yaml') as f:
        datas = yaml.safe_load(f)
        print(datas)
        batter_leve = datas['default']['batter_leve']
        print(batter_leve)
        km = datas['default']['km']
        print(km)
        myebycle = EBuycle(batter_leve)

        myebycle.run(km)




