from testmodule import warrior
from testmodule import weapon
from testmodule import barbarian


sword = weapon(10,5,5,"sword")
sword_and_sheld=weapon(12,5,12,"sword_and_sheld")
axe=weapon(12,12,5,"axe")


if __name__ == "__main__":
    peter = barbarian(name = "Peter",weapon = axe)
    bob = warrior(200,5,"Bob",weapon = sword)
    #print(peter.__dict__) # print all varriavles object peter
    (peter.greet())
    (bob.greet())
    #peter.attack(bob)
    #print(isinstance(peter,warrior))
    #type(peter)
    peter.fight(bob)
