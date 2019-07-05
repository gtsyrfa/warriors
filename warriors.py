from random import randint

class Weapon:
    def __init__(self, damage=3,attack=3,defence=3,name="hands"):
        self.damage = damage
        self.attack = attack
        self.defence = defence
        self.name = name





HAND = Weapon()


class Warrior:
    def __init__(self,hp=100,strong=3,name="noName",weapon=HAND):
        self.name = name
        self.currenthp = hp
        self.strong = strong
        self.weapon = weapon
        self.sumdmg = self.strong + self.weapon["damage"]

    def attack(self,target):
        if isinstance(target,Warrior):
            sumattack=self.weapon["attack"]+self.strong+randint(1,20)
            print(f"{self.name} try to attack {target.name} "\
                  f"witch attack {sumattack}")

            summdef = target.weapon["defence"]+target.strong+randint(1,20)
            print(f"{target.name} try to defence {summdef}")
            attack_difference = sumattack-summdef
            if (attack_difference>0):
                dmg=randint((self.sumdmg//2),self.sumdmg)
                target.currenthp -=  dmg
                print(f"Attack is successful. Damage is {dmg}")
            else:
                print("Miss!")
            print(f"{target.name} after attack have {target.currenthp} HP")
            return(attack_difference)
        else:
            print("only warriors can attack each other")
            return 0



    def greet(self):
        print(f'{self.name} is fighter with {self.currenthp} HP '\
              f'and {self.strong} basedamage. He weaponed is '\
              f'{self.weapon} witch damage {self.weapon["damage"]}')
    
    
    
    def fight(self,target):
        if self.currenthp<=0:
            print(f"{target.name} WIN!")
        else:
                type(self).attack(self,target)
                type(self).fight(target,self)




class Barbarian(Warrior):
    def attack(self,target):
        '''BARBARIAN can strike twice if him ANGRY'''
        attack_difference = (Warrior.attack(self,target))
        if attack_difference>5:
            print("Second attack with ANGRY!")
            Warrior.attack(self,target)