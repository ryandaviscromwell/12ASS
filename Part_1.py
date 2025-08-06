import easygui

Monster_cards = {
        "STO": {"name": "Stoneling","strength": 7,"speed": 1,"stealth": 25,"cunning": 15},
        "VEX": {"name": "Vexscream", "strength": 1, "speed": 6, "stealth": 21, "cunning": 19},
        "DAW": {"name": "Dawnmirage", "strength": 5, "speed": 15, "stealth": 18, "cunning": 22},
        "BLA": {"name": "Blazegolem", "strength": 15, "speed": 20, "stealth": 23, "cunning": 6},
        "WEB": {"name": "Websnake", "strength": 7, "speed": 15, "stealth": 10, "cunning": 5},
        "MOL": {"name": "Moldvine", "strength": 21, "speed": 18, "stealth": 14, "cunning": 5}, 
        "VOR": {"name": "Vortexwing", "strength": 19, "speed": 13, "stealth": 19, "cunning": 2},
        "ROT": {"name": "Rotthing", "strength": 16, "speed": 7, "stealth": 4,"cunning": 12},
        "FRO": {"name": "Froststep", "strength": 14, "speed": 14, "stealth": 17, "cunning": 4},
        "WIS": {"name": "Wispghoul", "strength": 17, "speed": 19, "stealth": 3, "cunning": 2},
        }

def new_cards():
        ID = easygui.enterbox("Enter cards ID")
        name = easygui.enterbox("Enter cards name")
        strength = easygui.integerbox("Enter cards strength value (1-25)")
        speed = easygui.integerbox("Enter cards speed (1-25)")
        stealth = easygui.integerbox("Enter cards stealth (1-25)")
        cunning = easygui.integerbox("Enter cards cunning (1-25)")
        print(ID,name,strength,speed,stealth,cunning)
    

ask = easygui.ynbox ("would you like to create any new monster cards?")
if ask == True:
        new_cards()
search = easygui.ynbox("would you like to search for a monster card?")
if search == True:
        choice = easygui.choicebox("Select a card you wish to edit", choices= list (Monster_cards.keys()))
        print(choice)
