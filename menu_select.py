def execute_display(menu_dict):
    for items, values in menu_dict.items():
        print("{}. {}".format(items, values.capitalize()))
    menu_selection = list (menu_dict.keys())
    selection = "#"
    while selection not in menu_selection:
        selection = input("Enter: ")
        if selection not in menu_selection:
            print("Invalid entry!")
    return selection, menu_dict[selection]
def menu_display():
    menu_dict = {
    '1': 'decimal_to_binary',
    '2': 'binary_to_decimal',
    'X': 'exit_program'
    }
    return menu_dict

def check_selection():
    try:
        return (False)
    except:
        print("Invalid input!!")
        return  (True, None)
def main():
    selection = menu_display()

    make_selection = True
    while make_selection:
        selection = input("Select an option from the menu:")
        make_selection = check_selection()


        print("You selcted {} and want to convert {}".format(selection, choice))

if __name__ == "__main__":
    main()
