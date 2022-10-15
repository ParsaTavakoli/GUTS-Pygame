from mob import Mob
import random
from player import Player
class Dragon(Mob):
    def __init__(self):
        self.health = 20
        
    def attack(self, player:Player):
        player.take_damage(random.randint(1,7))
    
    def take_damage(self, damage:int):
        self.health - damage