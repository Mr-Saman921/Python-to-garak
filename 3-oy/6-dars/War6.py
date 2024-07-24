
from random import randint
class War:

    def attack(self, enimy):
        print(f"{self.name} attack to {enimy.name}")
        shoot_count = randint(1, 10)
        damage = shoot_count * self.attack_power
        enimy.health -= damage
        if enimy.health <= 0:
            self.finish()

    def defence(self):
        pass

    def finish(self):
        print(f"Game over ! {self.name} winner")
