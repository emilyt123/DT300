#-------------------------------------------------------------------------------
# Name:        auction
# Purpose:      Sets a reserve price, collects bids and prints out a summary of the auction and the winning bid.
#
# Author:      tideswelle
#
# Created:     30/08/2016
# Copyright:   (c) tideswelle 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

def get_reserve():
    # Collects the reserve price from the auction manager
    #reserve = 0
    global reserve
    reserve = input("What is the reserve price?")
    print ("The reserve price is $" + reserve)
    return reserve

def auction(names, bids):
    # Collects bids
    print ("Auction has started.")
    global highest_bid
    highest_bid = 0
    global name
    name = ""
    while name.upper() != 'F':
        name = input("What is your name? (\"F\" to finish)")
        if name.upper() != "F":
            names.append(name)
            bid = (read_int("What is your bid, " + name + "?"))
            bids.append(bid)
            if bid > highest_bid:
                highest_bid = bid
                global highest_name
                highest_name = name
                print ("The highest bid so far is $" + str(bid) + " from " + name)
    return name
    return bids
    return highest_bid

def read_int(prompt):
    choice = -1;
    while choice == -1:
        try:
            choice = float(input(prompt))       # This means that bids can have many decimal places, could be changed later.
        except ValueError:
            print ("Not a valid integer")
    return choice

def show_report(winning_bid):
    # Prints summary of auction including highest bid
    #print(reserve)
    print(
    )
    if winning_bid >= float(reserve):
        print("The winning bid is $" + str(winning_bid) + " from " + highest_name)
    else:
        print("The auction did not reach reserve price.")
    i = 0
    for i in range(len(names)):
        print(str(names[i]) + " bid $" + str(bids[i]))
        i += 1

# Main program
#reserve = 0
names = []
bids = []
get_reserve()
auction(names, bids)
winning_bid = highest_bid
#print(highest_bid)
#print(winning_bid)
show_report(winning_bid)
