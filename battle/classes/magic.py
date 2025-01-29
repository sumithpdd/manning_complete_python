import random


class Spell:
    def __init__(self, name, cost, damage,type):
        self.name = name
        self.damage = damage
        self.cost = cost
        self.type = type
    
    def get_spell_name(self,i):
        return self.name
    
    def get_spell_mp_cost(self,i):
        return self.cost
    
    def generate_damage(self):
        low = self.damage - 15
        high = self.damage + 15

        return random.randrange(low,high)