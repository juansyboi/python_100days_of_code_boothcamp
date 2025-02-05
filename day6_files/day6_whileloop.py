#level up gacha

import random

player_hp = 100
player_mana = 50
player_damage = 5
player_level = 1

monster_hp = 10
monster_mana = 0
monster_damage = 2.5
monster_level = 1

def fight():
    monster_hp -= player_damage
    player_hp -= monster_damage

while player_hp > 0:
    fight()
