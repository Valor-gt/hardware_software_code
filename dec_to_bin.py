def decimal_to_binary(number):
    dec_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for number in number:
        if number.upper() not in dec_list: #check if the number is not in the dec list
            print("Not a decimal number")

        elif solve():

def solve():
                number = int(number)
                while number  > 0:            #keep dividing until 0
                    remainder = number % 2
                    number = number // 2
                    result = str(remainder) + result  #this line places the string in reverse, the computer reads from right to left
                    return result


def good_number_selection():
    while not good_number_selection:
        selection = input("Provide a decimal number:")
        good_number_selection = decimal_to_binary(number)
    print("Good job", number, "is a adecimal number!!!")


def main():
    num = str(input("Enter Decimal Number: "))
    print("Decimal {} to Binary: {}".format(num, decimal_to_binary(num)))

if __name__ == "__main__":
    main()
