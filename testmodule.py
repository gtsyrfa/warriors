class weapon:
    def __init__(self, damage=3):
        self.dmg=damage





class warrior:
    def __init__(self,hp=100,damage=10):
        self.currenthp = hp
        self.basedamage = damage


    #weapon weapinhand = hand
    #int BASEATTACK = 5
    #int BASEDEFFENCE = 10
    def attack(self,target):
        print(f"Has {self.basedamage} damage. His HP was {target.currenthp}.")
        target.currenthp = target.currenthp - self.basedamage #+ weapon.dmg
    #def get-damage(self,attacker):
    def meeting(self):
        return(f" is fighter with {self.currenthp} HP and {self.basedamage} damage")




peter = warrior()
bob = warrior(200,10)
print(peter.__dict__) # print all varriavles object peter
print(peter.meeting())
print(bob.meeting())
print("Peter attacked a bob")

peter.attack(bob)
print(peter.meeting())
print(bob.meeting())