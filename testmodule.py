from random import randint

class weapon:
    def __init__(self, damage=3,attack=3,defence=3,name="hands"):
        self.damage = damage
        self.attack = attack
        self.defence = defence
        self.name = name





HAND = weapon()

class warrior:
    def __init__(self,hp=100,strong=3,name="noName",weapon=HAND):
        self.name = name
        self.currenthp = hp
        self.strong = strong
        self.weapon = weapon
        self.sumdmg = self.strong + self.weapon.damage





    def attack(self,target):
        if isinstance(target,warrior):
            sumattack=self.weapon.attack+self.strong+randint(1,20)
            print(f"{self.name} try to attack {target.name} "\
                  f"witch attack {sumattack}")
            summdef = target.weapon.defence+target.strong+randint(1,20)
            print(f"{target.name} try to defence {summdef}")
            if (sumattack-summdef>0):
                __dmg=randint((self.sumdmg//2),self.sumdmg)
                target.currenthp -=  __dmg
                print(f"Attack is successful. Damage is { __dmg}")
            else:
                print("Miss!")
            print(f"{target.name} after attack have {target.currenthp} HP")
            return(sumattack-summdef)
        else:
            print("only warriors can attack each other")
            return 0
        


 
    def greet(self):
        print(f"{self.name} is fighter with {self.currenthp} HP "\
              f"and {self.strong} basedamage. He weaponed is "\
              f"{self.weapon.name} witch damage {self.weapon.damage}")
    
    
    
    def fight(self,target):
        if self.currenthp<0:
            print(f"{target.name} WIN!")
        else:
                type(self).attack(self,target)
                type(self).fight(target,self)




class barbarian(warrior):
    def attack(self,target):
        __attackdifference = (warrior.attack(self,target))
        #print("Debug>>>",__attackdifference)
        #print("Debug>>>",type(__attackdifference))
        if __attackdifference>5:
            print("Second attack witch FURRY!")
            warrior.attack(self,target)