from warriors import Warrior
from warriors import Weapon
from warriors import Barbarian

sword = Weapon(8, 5, 5, "sword")
sword_and_sheld = Weapon(12, 5, 12, "sword_and_sheld")
axe = Weapon(12, 12, 5, "axe")
# doublehandaxe={"damage": 15, "attack": 15, "defence": 2}

if __name__ == "__main__":
    peter = Barbarian(name="Peter", weapon=axe)
    bob = Warrior(200, 5, "Bob")
    # print(peter.__dict__) # print all varriavles object peter
    # (peter.greet())
    # (bob.greet())
    # peter.attack(bob)
    # print(isinstance(peter,warrior))
    # type(peter)
    peter.fight(bob)