#import so stuff works
import tkinter as tk
import tkinter.ttk as ttk

#import from other files
from armourtable import *
from weapontable import *

#Basic character and player info
tk_character_name = tk.Label(text = "Character name placeholder")
tk_player_name = tk.Label(text = "Player placeholder")
tk_lvl_class = tk.Label(text = "Level and class placeholder")
tk_char_race = tk.Label(text = "race placeholder")
tk_alignment = tk.Label(text = "alignment placeholder")
tk_experience = tk.Label(text = "experience placeholder")

#base stats
tk_strength = tk.Label(text = "Str + bonus")
tk_dexterity = tk.Label(text = "dex + bonus")
tk_constitution = tk.Label(text = "con + bonus")
tk_intellegence = tk.Label(text = "int + bonus")
tk_wisdom = tk.Label(text = "wis + bonus")
tk_charisma = tk.Label(text = "cha + bonus")
tk_passive_awareness = tk.Label(text = "passive awareness placeholder")

#Saves, HP, AC, move speed
tk_proficiency_bonus = tk.Label(text = "Prof placeholder")
tk_total_hitdice = tk.Label(text = "HitDice placeholder")
tk_max_hp = tk.Label(text = "Max HP placeholder")
tk_current_hp = tk.Label(text = "current HP placeholder")
tk_armor_class = tk.Label(text = "AC placeholder")
tk_flatfoot_ac = tk.Label(text =  "flatfoot XP placeholder")
tk_movement_speed = tk.Label(text = "move speed placeholder")
tk_str_save = tk.Label(text = "Str Save placeholder")
tk_dex_save = tk.Label(text = "Dex Save placeholder")
tk_con_save = tk.Label(text = "Con Save placeholder")
tk_int_save = tk.Label(text = "Int Save placeholder")
tk_wis_save = tk.Label(text = "Wis Save placeholder")
tk_cha_save = tk.Label(text = "Cha Save placeholder")

#skills
tk_acrobatics = tk.Label(text = "acrobatics placeholder")
tk_animal_handling = tk.Label(text = "animal handling placeholder")
tk_arcana = tk.Label(text = "arcana placeholder")
tk_athletics = tk.Label(text = "athletics placeholder")
tk_deception = tk.Label(text = "deception placeholder")
tk_history = tk.Label(text = "history placeholder")
tk_insight = tk.Label(text = "insight placeholder")
tk_intimidation = tk.Label(text = "intimidation placeholder")
tk_investigation = tk.Label(text = "investigation placeholder")
tk_medicine = tk.Label(text = "medicine placeholder")
tk_nature = tk.Label(text = "nature placeholder")
tk_perception = tk.Label(text = "perception placeholder")
tk_performance = tk.Label(text = "performance placeholder")
tk_persuasion = tk.Label(text = "persuasion placeholder")
tk_religion = tk.Label(text = "religion placeholder")
tk_slight_of_hand = tk.Label(text = "slight of hand placeholder")
tk_stealth = tk.Label(text = "stealth placeholder")
tk_survival = tk.Label(text = "survival placeholder")


window = tk.Tk()
character_name.pack()
lvl_class.pack()
alignment.pack()
window.mainloop()