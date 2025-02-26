# Name = (Display name, (light/medium/heavy), base AC, Str requirement, Stealth Dis True/False) - for Class constructor use
ARMOUR_PADDED = ("Padded Armor", "light", 11, 1, True)
ARMOUR_LEATHER = ("Leather Armor", "light", 11, 1, False)
ARMOUR_STUDDED = ("Studded Armor", "light", 12, 1, False)
ARMOUR_HIDE = ("Hide Armor", "medium", 12, 1, False)
ARMOUR_CHAINSHIRT = ("Chain Shirt", "medium", 13, 1, False)
ARMOUR_SCALE =  ("Scale Mail", "medium", 14, 1, True)
ARMOUR_BREASTPLATE = ("Breastplate", "medium", 14, 1, False)
ARMOUR_HALFPLATE = ("Half Plate", "medium", 15, 1, True)
ARMOUR_RINGMAIL = ("Ring Mail", "heavy", 14, 1, True)
ARMOUR_CHAINMAIL = ("Chain Mail", "heavy", 16, 13, True)
ARMOUR_SPLINT = ("Splint", "heavy", 17, 15, True)
ARMOUR_PLATE = ("Plate", "heavy", 18, 15, True)

class Armour:
    def __init__(self, name, weight, base_ac, str_req, stealth_disadvantage):
        self.name = name
        self.weight = weight
        self.base_ac =  base_ac
        self.str_req = str_req
        self.steal_dis = stealth_disadvantage

        
