class weapon:
    def __init__(self, damage=3):
        self.dmg=damage





class warrior:
    def __init__(self,hp=100,damage=10,name="noName"):
        self.name = name
        self.currenthp = hp
        self.basedamage = damage


    #weapon weapinhand = hand
    #int BASEATTACK = 5
    #int BASEDEFFENCE = 10
    def attack(self,target):
        print(f"{self.name} attacked {target.name} witch {self.basedamage}")
        target.currenthp = target.currenthp - self.basedamage #+ weapon.dmg
        print(f"{target.name} after attack have {target.currenthp}")
    #def get-damage(self,attacker):
    def meeting(self):
        return(f"is fighter with {self.currenthp} HP and {self.basedamage} damage")


