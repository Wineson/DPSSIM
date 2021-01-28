import csv
import OOP
import read_data as rd
import unit as u
import operator

Main = u.Unit("Amber","Prototype Crescent", 0, 1, 1, 1, 1)
sup1 = u.Unit("Diona","Prototype Crescent", 0, 1, 1, 1, 1)
sup2 = u.Unit("Fischl","Prototype Crescent", 0, 1, 1, 1, 1)
sup3 = u.Unit("Ganyu","Prototype Crescent", 0, 1, 1, 1, 1)
enemy = u.Enemy("Hilichurls")

# Creating a list of actions
class ActionList:
    def __init__ (self, main,sup1,sup2,sup3,enemy):
        MainActionDPS = u.UnitActionDPS(Main,enemy)
        sup1ActionDPS = u.UnitActionDPS(sup1,enemy)
        sup2ActionDPS = u.UnitActionDPS(sup2,enemy)
        sup3ActionDPS = u.UnitActionDPS(sup3,enemy)
        self.main_dps_normal_dps = MainActionDPS.normal_dps
        self.main_dps_charged_dps = MainActionDPS.charged_dps
        self.main_dps_skill_dps = MainActionDPS.skill_dps
        self.sup1_skill_dps = sup1ActionDPS.skill_dps
        self.sup2_skill_dps = sup2ActionDPS.skill_dps
        self.sup3_skill_dps = sup3ActionDPS.skill_dps
        self.main_dps_burst_dps = MainActionDPS.burst_dps
        self.sup1_burst_dps = sup1ActionDPS.burst_dps
        self.sup2_burst_dps = sup2ActionDPS.burst_dps
        self.sup3_burst_dps = sup3ActionDPS.burst_dps

    def asdict(self):
        return {'main_dps_normal_dps': self.main_dps_normal_dps, 'main_dps_charged_dps': self.main_dps_charged_dps,
        'main_dps_skill_dps': self.main_dps_skill_dps, 'main_dps_burst_dps': self.main_dps_burst_dps, 
        'sup1_skill_dps': self.sup1_skill_dps, 'sup1_burst_dps': self.sup1_burst_dps, 
        'sup2_skill_dps': self.sup2_skill_dps, 'sup2_burst_dps': self.sup2_burst_dps,
        'sup3_skill_dps': self.sup3_skill_dps, 'sup3_burst_dps': self.sup3_burst_dps }

TestActionList = ActionList(Main,sup1,sup2,sup3,enemy)
stats = TestActionList.asdict()

def main():
    print(TestActionList.main_dps_normal_dps)
    print(TestActionList.asdict())

    # Return Highest DPS Action
    print(max(stats, key=stats.get))

if __name__ == '__main__':
    main()