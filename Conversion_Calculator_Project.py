#Name:Tyler Bolton #Project Title:Conversion Calculator
#This program is supposed to allow you to convert numbers. You can convert decimal, binary, and hexadecimal.
def opening_statement():
    print("Hi there! Thank you for choosing this program. It's job is to convert numbers.")

def make_selection():
    selection = {
    '1' : 'binary to decimal',
    '2' : 'binary to hexadecimal',
    '3' : 'decimal to binary',
    '4' : 'decimal to hexadecimal, Not Coded',
    '5' : 'hexadecimal to binary, Not Coded',
    '6' : 'hexadecimal to decimal Not Coded',
    'X' : 'Done'
    }
    return selection

def display_menu(selection):
    for item, value in make_selection().items():
        print(item+"."+ value.replace('_',' ').capitalize())
    sel = input("Please make a selection")
    sels = list(make_selection().keys())
    if sel in sels[:-1]:
        print("You selected {} and want to convert {}".format(sel,make_selection()[sel]))
    elif sel.upper() == 'X':
        quit_sequence()
        user_input = 'Y' or 'N'
    else:
        print("Invalid selection")

    return sel

def quit_sequence():
    user_input == input("Would you like to quit 'Y' yes or 'N' no?")
    if user_input == 'Y':
        print("Thank you for using this program, have a nice day.")
    elif user_input == 'N':
        display_menu()
    # I haven't been able to get this to work as it keeps telling me that user_input
    # is not defined even though it has no reason to as I want it to be a memory address

def check_input_bin():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","A", "B", "C", "D", "E", "F"]

    good_number_bin = "0"
    # begin loop
    while good_number_bin in numbers:
    # Get the user to input a number
        user_numbers = input("Please enter a binary number")
        for number in user_numbers:
            if number not in numbers[:2]: # check if the number is not in the numbers list
                print("Not a binary number")
        good_number_bin = "#"
    print(user_numbers)
    return user_numbers

def check_input_dec():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","A", "B", "C", "D", "E", "F"]

    good_number_dec = "0"
    # begin loop
    while good_number_dec in numbers:
        user_numbers = input("Please enter a decimal number")
        for number in user_numbers:
            if number not in numbers[:10]:
                print("Not a deciaml number")
        good_number_dec = "#"
    print(user_numbers)
    return user_numbers

def binary_to_decimal(number):
    result = 0
    if len(number) > 0:
        power = len(str(number)) - 1 # determine greatest power
        for num in str(number):
            result += int(num) * 2 ** power
            power -= 1   # decrease by 1
        return result
def binary_to_hexadecimal(number):
    result = []
    output = []
    hex_list = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
			9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }
    while number != 0:
        result = number % 16 # error message not all arguments are converted during string formatting
        number /= 16
    result.append(number)
    result.reverse()
    for number in result:
        output.append(hex_list.get(number))
    return output

def decimal_to_binary(number):
    result = 0
    number = str(number)
    while number  != 0:            #keep dividing until 0
        remainder = number % 2  # error message not all arguments are converted during string formatting
        number = number // 2
        result = str(remainder) + result  #this line places the string in reverse, the computer reads from right to left
    return result





def main():
    opening_statement()
    run_this = True
    while run_this:
        selection = display_menu(make_selection())

        if selection == '1':
            number = check_input_bin()
            result = binary_to_decimal(number)
            print("The binary number {} converted to decimal is {}".format(number, result))
        elif selection == '2':
            number = check_input_bin()
            result = (binary_to_hexadecimal(number))
            print("The binary number {} converted to hexadecimal is {}".format(number, result))
        elif selection == '3':
            number = check_input_dec()
            result = decimal_to_binary(number)
            print("The decimal number {} converted to binary is {}".format(number, result))
        elif selection.upper() == 'X':
            run_this = False
    user_input = quit_sequence()





if __name__ == "__main__":
    main()
