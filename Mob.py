import abc
from player import Player
class Mob:
    @abc.abstractmethod
    def take_damage(self):
        pass
    def attack(self, player:Player):
        pass