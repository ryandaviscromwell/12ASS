import easygui

TITLE_NAME = "Monster Cards"
max = 25
min = 1


#This is my dictionary with all the preset cards
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

#This is the main menu of the program which you will be sent to after your chosen actions.
def main(): 
    menu = easygui.buttonbox("Welcome to Monster cards creation program Select what you want to do", choices= ("Create New", "Delete", "Edit", "View Cards", "print", "Close"),title=(TITLE_NAME))
    if menu == "Create New":
         new_cards()        
    elif menu == "Delete":
         delete()
    elif menu == "Close":
         close()
    elif menu == "View Cards":
         view_cards()
    elif menu == "print":
         printy()
    elif menu == "Edit":
         edit()
#This is how te user creates new cards
def new_cards():
        ID = easygui.enterbox("Enter cards ID")
        name = easygui.enterbox (str("Enter cards name"))
        strength = easygui.integerbox("Enter cards strength value (1-25)", default= 10, lowerbound=(min), upperbound=(max))
        speed = easygui.integerbox("Enter cards speed (1-25)", default= 10, lowerbound=(min), upperbound=(max))
        stealth = easygui.integerbox("Enter cards stealth (1-25)", default= 10, lowerbound=(min), upperbound=(max))
        cunning = easygui.integerbox("Enter cards cunning (1-25)", default= 10, lowerbound=(min), upperbound=(max))
        Monster_cards[ID] = {
            "name": name,
            "strength": strength,
            "speed": speed,
            "stealth": stealth,
            "cunning": cunning,
        }
        main()

    #Asks user if they want to search to edit a card            
def edit():
    search = easygui.buttonbox("would you like to search for a monster card to edit?", choices= ("search", "back"),title=(TITLE_NAME))
        #Shows the user all the cards they can choose from to edit
    if search == "search":
            name_to_key = {card["name"]: key for key, card in Monster_cards.items()}
            choice = easygui.choicebox("Select the card you want to edit",
                choices=list(name_to_key.keys()),title=(TITLE_NAME))
            if choice:
                card_delete = name_to_key[choice]
                card = Monster_cards[card_delete]
                info = f"Name: {card['name']}\nStrength: {card['strength']}\nSpeed: {card['speed']}\nStealth: {card['stealth']}\nCunning: {card['cunning']}"
                del Monster_cards[card_delete]
                new_cards()
                easygui.msgbox("Card has been updated",title=(TITLE_NAME))
                main()
                   
                        
        #If the user presses back it takes them back to the main menu
    if search == "back":
        main()
    #Asks user if they want to delete any cards
def delete():
    deleteq = easygui.ynbox ("Would you like to delete any cards?",title=(TITLE_NAME))
    if deleteq == True:
        #Shows all the cards they can delete
        #Choose the card you want to delete
        name_to_key = {card["name"]: key for key, card in Monster_cards.items()}
        choice = easygui.choicebox("Select the card you want to delete",
                choices=list(name_to_key.keys()),title=(TITLE_NAME))
        if choice:
            card_delete = name_to_key[choice]
            card = Monster_cards[card_delete]
            info = "Are you sure you want to delete this card?" f"\n\nName: {card['name']}\nStrength: {card['strength']}\nSpeed: {card['speed']}\nStealth: {card['stealth']}\nCunning: {card['cunning']}"
            easygui.msgbox(info, title=f"Details for {choice}")
            del Monster_cards[card_delete]
            main()
        #Takes you back to main menu
    if deleteq == False:
        main()      
def printy():
    print_cards = easygui.ynbox ("would you like to print the full monster card catalogue?",title=(TITLE_NAME))
    if print_cards == True:
        print(Monster_cards)
        easygui.msgbox("Succsefully printed Monster cards",title=(TITLE_NAME))
        main()
    else:
        main()
def view_cards():
        #Shows user ID's of all cards for the user to select and view
    view = easygui.choicebox("select the card you want to view",choices= list (Monster_cards.keys()),title=(TITLE_NAME))
    if view:
        card = Monster_cards[view]
        info = f"Name: {card['name']}\nStrength: {card['strength']}\nSpeed: {card['speed']}\nStealth: {card['stealth']}\nCunning: {card['cunning']}"
        easygui.msgbox(info, title=f"Details for {view}")
        main()
    #Closes the program
def close():
     quit

main()