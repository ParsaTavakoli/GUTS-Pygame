from secrets import randbits
from mob import Mob
import abc
import random

class Player:
        
    def roll_dice(self, start, stop):
        pass

    def normal_attack(self, mob:Mob):
        pass
    
    def special_attack(self, mob:Mob):
        pass

    def take_damage(self, damage:int):
        pass
    
    def run_away(self, mob:Mob):
        pass