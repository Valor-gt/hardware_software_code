def check_selection(numbers):  # verify if its a hexadecimal
    hex_list = ["A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for numbers in numbers:
        if numbers.upper() not in hex_list: #check if the number is not in the hex list
            print("Not a hexadecimal number")
            return(False)
    return(True)

def main():
    good_selection = False
    while not good_selection:
        selection = input("Provide a hexadecimal number:")
        good_selection = check_selection(selection)
    print("Good job", selection, "is a hexadecimal number!!!")


if __name__ == "__main__":
    main()
