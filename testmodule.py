class weapon:
    dmg=0


hand = weapon
hand.dmg=0

class warrior:
    BASEHP = 120
    BASEDAMAGE = 10
    currenthp = BASEHP
    #weapon weapinhand = hand
    #int BASEATTACK = 5
    #int BASEDEFFENCE = 10
    def attack(self,weapon,target):
        return (target.currenthp - BASEDAMAGE) #+ weapon.dmg
    #def block(self):

    def meeting(self):
        return(" is fighter with {} HP and {} damage".format(
            self.currenthp,self.BASEDAMAGE))




peter = warrior
print(warrior.meeting(peter))


bob = warrior
bob.currenthp*=2

print(warrior.meeting(bob))