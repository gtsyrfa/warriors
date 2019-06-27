class weapon:
    def __init__(self, damage=3):
        self.dmg=damage





class warrior:
    def __init__(self,hp=120,damage=10):
        self.currenthp = hp
        self.basedamage = damage


    #weapon weapinhand = hand
    #int BASEATTACK = 5
    #int BASEDEFFENCE = 10
    def attack(self,target):
        return (target.currenthp - self.basedamage) #+ weapon.dmg
    #def block(self):

    def meeting(self):
        return(" is fighter with {} HP and {} damage".format(
            self.currenthp,self.basedamage))




peter = warrior()
bob = warrior(115,15)
print(peter.__dict__)
print(peter.meeting())
print(bob.meeting())
print("Peter attacked a bob")
bob.currenthp =(peter.attack(target=bob))

print(peter.meeting())
print(bob.meeting())