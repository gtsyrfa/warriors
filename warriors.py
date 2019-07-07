from random import randint


class Weapon:
    def __init__(self, damage=3, attack=3, defence=3, name=""):
        self.damage = damage
        self.attack = attack
        self.defence = defence
        self.name = name


HAND = Weapon(name="Hand")


class Warrior:
    def __init__(self, hp=100, strong=3, name="noName", weapon=HAND):
        self.name = name
        self.current_hp = hp
        self.strong = strong
        self.weapon = weapon
        self.sum_dmg = self.strong + self.weapon.damage

    def __attack(self, target):
        if isinstance(target, Warrior):
            sum_attack = self.weapon.attack + self.strong+randint(1, 20)
            print(f"{self.name} try to attack {target.name} "\
                  f"witch attack {sum_attack}")

            sum_def = target.weapon.defence+target.strong+randint(1, 20)
            print(f"{target.name} try to defence {sum_def}")
            attack_difference = sum_attack-sum_def
            if (attack_difference > 0):
                dmg = randint((self.sum_dmg // 2), self.sum_dmg)
                target.current_hp -= dmg
                print(f"Attack is successful. Damage is {dmg}")
            else:
                print("Miss!")
            print(f"{target.name} after attack have {target.current_hp} HP")
            return(attack_difference)
        else:
            print("only warriors can attack each other")
            return None

    def greet(self):
        print(f'{self.name} is fighter with {self.current_hp} HP '\
              f'and {self.strong} base damage. He weaponed is '\
              f'{self.weapon} witch damage {self.weapon.damage}')
    
    def fight(self, target):
        if self.current_hp <= 0:
            print(f"{target.name} WIN!")
        else:
            type(self).__attack(self, target)
            type(self).fight(target, self)


class Barbarian(Warrior):
    def __attack(self, target):
        """BARBARIAN can strike twice if him ANGRY"""
        attack_difference = (Warrior.attack(self, target))
        if attack_difference > 5:
            print("Second attack with ANGRY!")
            Warrior.attack(self, target)
            return None
