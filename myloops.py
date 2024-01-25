def while_counter(num):
    while num >= 100:
        print("While count:{}".format(num))
        num += -2

def for_counter(num):
    for count in range(num,-2, -2):
        print("For count:{}".format(count))

def main():
    counter = 100
    while_counter(counter)
    for_counter(counter)

if __name__ == "__main__":
    main()
