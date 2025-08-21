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
while True:
    test = easygui.buttonbox("select what you want to do", choices= ("Create New", "Delete", "Edit", "View Cards", "Close"))
    def new_cards():
            ID = easygui.enterbox("Enter cards ID")
            name = easygui.enterbox("Enter cards name")
            strength = easygui.integerbox("Enter cards strength value (1-25)", lowerbound=1, upperbound=25)
            speed = easygui.integerbox("Enter cards speed (1-25)", lowerbound=1, upperbound=25)
            stealth = easygui.integerbox("Enter cards stealth (1-25)", lowerbound=1, upperbound=25)
            cunning = easygui.integerbox("Enter cards cunning (1-25)", lowerbound=1, upperbound=25)
            print(ID,name,strength,speed,stealth,cunning)
            Monster_cards[ID] = {
                "name": name,
                "strength": strength,
                "speed": speed,
                "stealth": stealth,
                "cunning": cunning,
            }
            print(Monster_cards)
    if test == "Create new":   
        while True:
            ask = easygui.ynbox ("would you like to create any new monster cards?")
            if ask == True:
                new_cards()
            else:
                break
                
    if test == "Edit":
        search = easygui.buttonbox("would you like to search for a monster card to edit?", choices= ("search", "back"))
        if search == "search":
                while True:
                    choice = easygui.choicebox("Select a card you wish to edit", choices= list (Monster_cards.keys()))
                    if choice:
                        card = Monster_cards[choice]
                        info = f"Name: {card['name']}\nStrength: {card['strength']}\nSpeed: {card['speed']}\nStealth: {card['stealth']}\nCunning: {card['cunning']}"
                        easygui.msgbox(info, title=f"Details for {choice}")
                        del Monster_cards[choice]
                        new_cards()
                        easygui.msgbox("Card has been updated")
                        q = easygui.ynbox("Would you like to edit any other cards?")
                        if q == True:
                                ()
                        else:
                            break
        if search == "back":
            ()
    if test == "delete":               
        deleteQ = easygui.ynbox ("Would you like to delete any cards?")
        if deleteQ == True:
            while True:
                delete = easygui.choicebox("select the card you want to delete",choices= list (Monster_cards.keys()))
                if delete:
                    card_delete = Monster_cards[delete]
                    makeing_sure = easygui.ynbox("Are you sure you want to delete this card?")
                    if makeing_sure == True:
                        del Monster_cards[delete]
                        break
                    else:
                        break
        if deleteQ == False:
           ()
    if test == "View cards":
        view = easygui.choicebox("select the card you want to view",choices= list (Monster_cards.keys()))
        if view:
            card = Monster_cards[view]
            info = f"Name: {card['name']}\nStrength: {card['strength']}\nSpeed: {card['speed']}\nStealth: {card['stealth']}\nCunning: {card['cunning']}"
            easygui.msgbox(info, title=f"Details for {view}")
    if test == "close":
        break
