#Name = ("Display Name", "simple/martial", "damage die", "damage type", "property 1", "property 2", "property 3", "Range")
#Melee weapons

WEAPON_CLUB = ("Club", "Simple Melee", "1d4", "bludgeoning", "light", None, None, None)
WEAPON_DAGGER = ("Dagger", "Simple Melee", "1d4", "piercing", "light", "finesse", "thrown", "20/60")
WEAPON_GREATCLUB = ("Greatclub", "Simple Melee", "1d8", "bludgeoning", "two-handed", None, None, None)
WEAPON_HANDAXE = ("Handaxe", "Simple Melee", "1d6", "slashing", "light", "thrown", None, "20/60")
WEAPON_JAVELIN = ("Javelin", "Simple Melee", "1d6", "piercing", "Thrown", None, None, "30/120")
WEAPON_LIGHTHAMMER = ("Light hammer", "Simple Melee", "1d4", "bludgeoning", "light", "thrown", None, "20/60")
WEAPON_MACE = ("Mace", "Simple Melee", "1d6", "bludgeoning", None, None, None, None)
WEAPON_QUARTERSTAFF = ("Quarterstaff", "Simple Melee", "1d6", "bludgeoning", "versatile - 1d8", None, None, None)
WEAPON_SICKLE = ("Sickle", "Simple Melee", "1d4", "slashing", "light", None, None, None)
WEAPON_SPEAR = ("Spear", "Simple Melee", "1d6", "piercing", "thrown", "versatile - 1d8", None, "20/60")
WEAPON_BATTLEAXE = ("Battleaxe", "Martial Melee", "1d8", "slashing", "versatile - 1d10", None, None, None)
WEAPON_FLAIL = ("Flail", "Martial Melee", "1d8", "bludgeoning", None, None, None, None)
WEAPON_GLAIVE = ("Glaive", "Martial Melee", "1d10", "slashing", "heavy", "reach", "two-handed", None)
WEAPON_GREATAXE = ("Greataxe", "Martial Melee", "1d12", "slashing", "heavy ", "two-handed", None, None)
WEAPON_GREATSWORD = ("Greatsword", "Martial Melee", "2d6", "slashing", "heavy", "two-handed", None, None)
WEAPON_HALBERD = ("Halberd", "Martial Melee", "1d10", "slashing", "heavy", "reach", "two-handed", None)

#Name = ("Display Name", "simple/martial", "damage die", "damage type", "property 1", "property 2", "property 3", "hcbiab", "range")
#Ranged weapons ...why do you have to be like this, heavy crossbow?!  Who hurt you? 9082    3r


class MeleeWeapon:
    def __init__(self, name, sim_mar, dice, damage_type, prop_1, prop_2, prop_3, range):
        self.name = name
        self.sim_mar = sim_mar
        self.dice = dice
        self.damage_type = damage_type
        self.prop_1 = prop_1
        self.prop_2 = prop_2
        self.prop_3 = prop_3
        self.range = range

class RangedWeapon:
    def __init__(self, name, sim_mar, dice, damage_type, prop_1, prop_2, prop_3, hciab, range):
        self.name = name
        self.sim_mar = sim_mar
        self.dice = dice
        self.damage_type = damage_type
        self.prop_1 = prop_1
        self.prop_2 = prop_2
        self.prop_3 = prop_3
        self.hciab = hciab
        self.range = range