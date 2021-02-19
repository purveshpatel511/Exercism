import math
import random

def modifier(value):
    val = (value - 10) / 2
    return int(math.floor(val))

class Character:
    def __init__(self):
        strength_list = [random.randint(1,6) for i in range(4)]
        strength_list.sort()
        self.strength = strength_list[-1]+strength_list[-2]+strength_list[-3]

        dexterity_list = [random.randint(1,6) for i in range(4)]
        dexterity_list.sort()
        self.dexterity = dexterity_list[-1]+dexterity_list[-2]+dexterity_list[-3]

        constitution_list = [random.randint(1,6) for i in range(4)]
        constitution_list.sort()
        self.constitution = constitution_list[-1]+constitution_list[-2]+constitution_list[-3]

        intelligence_list = [random.randint(1,6) for i in range(4)]
        intelligence_list.sort()
        self.intelligence = intelligence_list[-1]+intelligence_list[-2]+intelligence_list[-3]

        wisdom_list = [random.randint(1,6) for i in range(4)]
        wisdom_list.sort()
        self.wisdom = wisdom_list[-1]+wisdom_list[-2]+wisdom_list[-3]

        charisma_list = [random.randint(1,6) for i in range(4)]
        charisma_list.sort()
        self.charisma = charisma_list[-1]+charisma_list[-2]+charisma_list[-3]
        
        self.hitpoints = 10 + modifier(self.constitution)
        pass

    def ability(self):
        return self.constitution

c = Character()