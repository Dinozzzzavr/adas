from random import randint
class Human:
    def __init__(self,name,health):
        self._name = name
        self._health = health
    # Нанесение урона
    def attack(self,enemy):
       damage =  randint(1,10)
       enemy.get_damage(damage)
       print(f"{self._name} наносит персонажу {enemy._name} {damage} урона!")
    def get_damage(self,damage):
        self._health-=damage
        print(f"{self._name} получает урон {damage} урона! Текущее здоровье - {self._health}")
    def get_healing(self,enemy):
        health = randint(5,15)
        enemy.get_health(health)
        print(f"{self._name} восстанавливает {health} здровья. Текущее здровье - {self._health}")
human1 = Human(name="Егор", health=80)
human2 = Human(name="Слава", health=50)
print(human1.attack(human2))


