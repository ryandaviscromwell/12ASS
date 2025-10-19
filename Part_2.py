"""This is for making monster cards."""
import easygui

# Name of the dictionary
TITLE_NAME = "Monster cards"
# maximum number for card details
max = 25
# minimium number for card details
min = 1


# This is my dictionary with all the preset cards
Monster_cards = {
        "STO": {"name": "Stoneling", "strength": 7, "speed": 1,
                "stealth": 25, "cunning": 15},
        "VEX": {"name": "Vexscream", "strength": 1, "speed": 6,
                "stealth": 21, "cunning": 19},
        "DAW": {"name": "Dawnmirage", "strength": 5, "speed": 15,
                "stealth": 18, "cunning": 22},
        "BLA": {"name": "Blazegolem", "strength": 15, "speed": 20,
                "stealth": 23, "cunning": 6},
        "WEB": {"name": "Websnake", "strength": 7, "speed": 15,
                "stealth": 10, "cunning": 5},
        "MOL": {"name": "Moldvine", "strength": 21, "speed": 18,
                "stealth": 14, "cunning": 5},
        "VOR": {"name": "Vortexwing", "strength": 19, "speed": 13,
                "stealth": 19, "cunning": 2},
        "ROT": {"name": "Rotthing", "strength": 16, "speed": 7,
                "stealth": 4, "cunning": 12},
        "FRO": {"name": "Froststep", "strength": 14, "speed": 14,
                "stealth": 17, "cunning": 4},
        "WIS": {"name": "Wispghoul", "strength": 17, "speed": 19,
                "stealth": 3, "cunning": 2},
        }
# This is the main menu where you choose what to do


def main():
    """Go to main menu of program."""
    menu = easygui.buttonbox("Welcome to Monster cards creation program"
                             " Select what you want to do",
                             choices=("Create New", "Delete",
                                      "Edit", "View Cards", "print",
                                      "Close"), title=(TITLE_NAME))
    if menu == "Create New":
        # runs code for new cards
        new_cards()
    elif menu == "Delete":
        # runs code for delete
        delete()
    elif menu == "Close":
        # runs code for close
        close()
    elif menu == "View Cards":
        # runs code for view cards
        view_cards()
    elif menu == "print":
        # runs code for print
        printy()
    elif menu == "Edit":
        # runs code for edit
        edit()
# This is the code to create new cards


def new_cards():
    """Create new cards."""
    id = easygui.enterbox("Enter cards ID")
    while True:
        name = easygui.enterbox(str("Enter cards name"))
        if name == "":
            easygui.msgbox("Please enter a name")
        else:
            break

    strength = easygui.integerbox("Enter cards strength value (1-25)",
                                  default=10, lowerbound=(min),
                                  upperbound=(max))
    speed = easygui.integerbox("Enter cards speed (1-25)", default=10,
                               lowerbound=(min), upperbound=(max))
    stealth = easygui.integerbox("Enter cards stealth (1-25)", default=10,
                                 lowerbound=(min), upperbound=(max))
    cunning = easygui.integerbox("Enter cards cunning (1-25)", default=10,
                                 lowerbound=(min), upperbound=(max))
    Monster_cards[id] = {
        "name": name,
        "strength": strength,
        "speed": speed,
        "stealth": stealth,
        "cunning": cunning,
    }
    main()
# Asks user if they want to search to edit a card


def edit():
    """Edit the cards."""
    search = easygui.buttonbox("would you like to search for"
                               " a monster card to edit?",
                               choices=("search", "back"), title=(TITLE_NAME))
    # Shows the user all the cards they can choose from to edit
    if search == "search":
        name_to_key = {card["name"]: key for key,
                       card in Monster_cards.items()}
        # The user chooses card they want to edit
        choice = easygui.choicebox("Select the card you want to edit",
                                   choices=list(name_to_key.keys()),
                                   title=(TITLE_NAME))
        if choice:
            card_delete = name_to_key[choice]
            del Monster_cards[card_delete]
            new_cards()
            # card has been changed and is in the monster cards dictionary
            easygui.msgbox("Card has been updated", title=(TITLE_NAME))
            main()

    # If the user presses back it takes them back to the main menu
    if search == "back":
        main()
# Asks user if they want to delete any cards


def delete():
    """Delete the cards."""
    deleteq = easygui.ynbox("Would you like to delete any cards?",
                            title=(TITLE_NAME))
    # shows user all cards they can delete
    if deleteq is True:
        name_to_key = {card["name"]: key for key,
                       card in Monster_cards.items()}
        # user selects card they want to delete
        choice = easygui.choicebox("Select the card you want to delete",
                                   choices=list(name_to_key.keys()),
                                   title=(TITLE_NAME))
        if choice:
            card_delete = name_to_key[choice]
            card = Monster_cards[card_delete]
            # Shows the info card and asks if they still want to delete
            info = easygui.ynbox(
                "Are you sure you want to delete this card?"
                f"\n\nName: {card['name']}"
                f"\nStrength: {card['strength']}"
                f"\nSpeed: {card['speed']}"
                f"\nStealth: {card['stealth']}"
                f"\nCunning: {card['cunning']}"
            )
            if info is True:
                del Monster_cards[card_delete]
                easygui.msgbox("Card succsefully deleted")
                main()
            else:
                main()
        # Takes you back to main menu
    if deleteq is False:
        main()


def printy():
    """Print cards."""
    # Asks user if they want to print cards
    print_cards = easygui.ynbox("would you like to print the full monster"
                                " card catalogue?", title=(TITLE_NAME))
    if print_cards is True:
        # Cards are printed if yes
        print(Monster_cards)
        easygui.msgbox("Succsefully printed Monster cards", title=(TITLE_NAME))
        main()
    else:
        # If no you go back to main menu
        main()


def view_cards():
    """View any card."""
    # Shows user names of all cards for the user to select and view
    view = easygui.choicebox("select the card you want to view",
                             choices=list(Monster_cards.keys()),
                             title=(TITLE_NAME))
    # the details of selected card are shown
    if view:
        card = Monster_cards[view]
        info = (
            f"Name: {card['name']}"
            f"\nStrength: {card['strength']}"
            f"\nSpeed: {card['speed']}"
            f"\nStealth: {card['stealth']}"
            f"\nCunning: {card['cunning']}"
        )
        easygui.msgbox(info, title=f"Details for {view}")
        # Takes you back to main menu
        main()
# Closes the program


def close():
    """Quit the program."""
    quit
# This opens up the program at the main menu


main()
