def get_menu():
    menu_dict = {
        '1':'apples',
        '2':'bananas',
        '3':'cherries',
        '4':'pears',
        'x':'done_ordering'
    }
    return menu_dict

def display_menu(menu_dict):
    for items, values in menu_dict.items():
        print(items+"."+ values.replace('_',' ').capitalize())
    menu_selection = input("What would you like to buy? ").upper()
    if input() == ('1', '2', '3', '4'):
        print("You selected {}".format(menu_dict[menu_selection]))
    elif input() == (''):
        print("You haven't selected anything, please select the item you would like to purchase. ")


    return menu_selection

def display_purchases(item_list):
    del item_list[-1]
    print("You purchased {} items".format(len(item_list)), end="")
    print(*item_list, sep=", ", end=".\n")

def main():
    menu_selection = ''
    item_list = []
    while menu_selection !='X':
        menu_dict = get_menu()
        menu_selection = display_menu(menu_dict)
        item_list.append(menu_dict[menu_selection])
        input("Hit Enter to Continue!!")

    display_purchases(item_list)

if __name__ == "__main__":
    main()
