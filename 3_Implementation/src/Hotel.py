import random
import datetime
import sys

NAME = []
PHONE_No = []
ADD = []
Checkin_Date = []
Checkout_date = []
ROOM = []
PRICE = []
RC = []
p = []
ROOM_No = []
Customer_Id = []
Day = []

# Global Variable Declaration
i = 0

# Home Function
def Home():
    print("\n\t\t\t\t\t\t WELCOME TO SYSTEM \n")
    print("\t\t\t\t\t\t   NAMAN THAKUR")
    print("Enter your choice: \n")
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 ROOMs Info\n")
    print("\t\t\t 3 Payment\n")
    print("\t\t\t 4 Record\n")
    print("\t\t\t 5 Exit\n")

    c_h = int(input("->"))

    if c_h == 1:
        print(" ")
        Booking()

    elif c_h == 2:
        print(" ")
        ROOMsinfo()

    elif c_h == 3:
        print(" ")
        payment()

    elif c_h == 4:
        print(" ")
        record()

    #elif c_h == 5:
       # print(" ")
      #  record()

    else:
        exit()
    return 0
# Function used in booking

def date(c):
    if c[2] <= 2022:

        if c[1] != 0 and 12 >= c[1] >= 4:

            if c[1] == 2 and c[0] != 0 and c[0] <= 28:

                if c[2] % 4 == 0 and c[0] <= 29:
                    pass

                elif c[0] < 29:
                    pass

                else:
                    print("Invalid date\n")
                    NAME.pop(i)
                    PHONE_No.pop(i)
                    ADD.pop(i)
                    Checkin_Date.pop(i)
                    Checkout_date.pop(i)
                    Booking()

            # if month is odd & less than equal
            # to 7th  month
            elif c[1] <= 7 and c[1] % 2 != 0 and c[0] <= 31:
                pass

            # if month is even & less than equal to 7th
            # month and not 2nd month
            elif c[1] <= 7 and c[1] % 2 == 0 and c[0] <= 30 and c[1] != 2:
                pass

            # if month is even & greater than equal
            # to 8th  month
            elif c[1] >= 8 and c[1] % 2 == 0 and c[0] <= 31:
                pass

            # if month is odd & greater than equal
            # to 8th  month
            elif c[1] >= 8 and c[1] % 2 != 0 and c[0] <= 30:
                pass

            else:
                print("Invalid date\n")
                NAME.pop(i)
                PHONE_No.pop(i)
                ADD.pop(i)
                Checkin_Date.pop(i)
                Checkout_date.pop(i)
                Booking()

        else:
            print("Invalid date\n")
            NAME.pop(i)
            PHONE_No.pop(i)
            ADD.pop(i)
            Checkin_Date.pop(i)
            Checkout_date.pop(i)
            Booking()

    else:
        print("Invalid date\n")
        NAME.pop(i)
        PHONE_No.pop(i)
        ADD.pop(i)
        Checkin_Date.pop(i)
        Checkout_date.pop(i)
        Booking()

# Booking function
def Booking():
    # used global keyword to
    # use global variable 'i'
    global i
    print(" BOOKING ROOMS")
    print(" ")

    while 1:
        n = str(input("NAME: "))
        p_1 = str(input("PHONE No.: "))
        a = str(input("ADDress: "))

        # checks if any field is not empty
        if n != "" and p_1 != "" and a != "":
            NAME.append(n)
            ADD.append(a)
            break

        else:
            print("\tNAME, PHONE no. & ADDress cannot be empty..!!")

    cii = str(input("Check-In: "))
    Checkin_Date.append(cii)
    cii = cii.split('/')
    c_i = cii
    c_i[0] = int(c_i[0])
    c_i[1] = int(c_i[1])
    c_i[2] = int(c_i[2])
    date(c_i)

    coo = str(input("Check-Out: "))
    Checkout_date.append(coo)
    coo = coo.split('/')
    c_o = coo
    c_o[0] = int(c_o[0])
    c_o[1] = int(c_o[1])
    c_o[2] = int(c_o[2])

    # checks if check-out date falls after
    # check-in date
    if c_o[1] < c_i[1] and c_o[2] < c_i[2]:

        print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
        NAME.pop(i)
        ADD.pop(i)
        Checkin_Date.pop(i)
        Checkout_date.pop(i)
        Booking()
    elif c_o[1] == c_i[1] and c_o[2] >= c_i[2] and c_o[0] <= c_i[0]:

        print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
        NAME.pop(i)
        ADD.pop(i)
        Checkin_Date.pop(i)
        Checkout_date.pop(i)
        Booking()
    else:
        pass

    date(c_o)
    d_1 = datetime.datetime(c_i[2], c_i[1], c_i[0])
    d_2 = datetime.datetime(c_o[2], c_o[1], c_o[0])
    d_ = (d_2 - d_1).Day
    Day.append(d_)

    print("----SELECT ROOM TYPE----")
    print(" 1. Standard Non-AC")
    print(" 2. Standard AC")
    print(" 3. 3-Bed Non-AC")
    print(" 4. 3-Bed AC")
    print(("\t\tPress 0 for ROOM PRICEs"))

    c_h = int(input("->"))

    # if-conditions to display alloted ROOM
    # type and it's PRICE
    if c_h == 0:
        print(" 1. Standard Non-AC - Rs. 3500")
        print(" 2. Standard AC - Rs. 4000")
        print(" 3. 3-Bed Non-AC - Rs. 4500")
        print(" 4. 3-Bed AC - Rs. 5000")
        c_h = int(input("->"))
    if c_h == 1:
        ROOM.append('Standard Non-AC')
        print("ROOM Type- Standard Non-AC")
        PRICE.append(3500)
        print("PRICE- 3500")
    elif c_h == 2:
        ROOM.append('Standard AC')
        print("ROOM Type- Standard AC")
        PRICE.append(4000)
        print("PRICE- 4000")
    elif c_h == 3:
        ROOM.append('3-Bed Non-AC')
        print("ROOM Type- 3-Bed Non-AC")
        PRICE.append(4500)
        print("PRICE- 4500")
    elif c_h == 4:
        ROOM.append('3-Bed AC')
        print("ROOM Type- 3-Bed AC")
        PRICE.append(5000)
        print("PRICE- 5000")
    else:
        print(" Wrong choice..!!")

    # randomly generating ROOM no. and customer
    # id for customer
    rn = random.randrange(40) + 300
    cid = random.randrange(40) + 10

    # checks if alloted ROOM no. & customer
    # id already not alloted
    while rn in ROOM_No or cid in Customer_Id:
        rn = random.randrange(60) + 300
        cid = random.randrange(60) + 10

    RC.append(0)
    p.append(0)

    if p_1 not in PHONE_No:
        PHONE_No.append(p_1)
    elif p_1 in PHONE_No:
        for n in range(0, i):
            if p_1 == PHONE_No[n]:
                if p[n] == 1:
                    PHONE_No.append(p_1)
    elif p_1 in PHONE_No:
        for n in range(0, i):
            if p_1 == PHONE_No[n]:
                if p[n] == 0:
                    print("\tPHONE no. already exists and payment yet not done..!!")
                    NAME.pop(i)
                    ADD.pop(i)
                    Checkin_Date.pop(i)
                    Checkout_date.pop(i)
                    Booking()
    print("")
    print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
    print("ROOM No. - ", rn)
    print("Customer Id - ", cid)
    ROOM_No.append(rn)
    Customer_Id.append(cid)
    i = i + 1
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()
    return 0
# ROOMS INFO
def ROOMsinfo():
    print("         ------ HOTEL ROOMS INFO ------")
    print("")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("ROOM amenities include: 1 Double Bed, Television, TelePHONE,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washROOM with hot/cold water.\n")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("ROOM amenities include: 1 Double Bed, Television, TelePHONE,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washROOM with hot/cold water + Window/Split AC.\n")
    print("3-Bed NON-AC")
    print("---------------------------------------------------------------")
    print("ROOM amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("TelePHONE, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washROOM with hot/cold water.\n")
    print("3-Bed AC")
    print("---------------------------------------------------------------")
    print("ROOM amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("TelePHONE, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washROOM with hot/cold water + Window/Split AC.\n\n")
    print()
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()

# PAYMENT FUNCTION
def payment():
    P_H = str(input("PHONE Number: "))
    global i
    f = 0

    for n in range(0, i):
        if P_H == PHONE_No[n]:

            # checks if payment is
            # not already done
            if p[n] == 0:
                f = 1
                print(" Payment")
                print(" --------------------------------")
                print("  MODE OF PAYMENT")

                print("  1- Credit/Debit Card")
                print("  2- Paytm/PHONEPe/Gpay")
                print("  3- Using UPI")
                print("  4- Cash")
                x = int(input("-> "))
                print("\n  Amount: ", (PRICE[n] * Day[n]) + RC[n])
                print("\n            Pay For SHAILAKSHI")
                print("  (y/n)")
                c_h = str(input("->"))

                if c_h == 'y' or c_h == 'Y':
                    print("\n\n --------------------------------")
                    print("           Naman Thakur")
                    print(" --------------------------------")
                    print("              Bill")
                    print(" --------------------------------")
                    print(" NAME: ", NAME[n], "\t\n PHONE No.: ", PHONE_No[n], "\t\n ADDress: ", ADD[n], "\t")
                    print("\n Check-In: ", Checkin_Date[n], "\t\n Check-Out: ", Checkout_date[n], "\t")
                    print("\n ROOM Type: ", ROOM[n], "\t\n ROOM Charges: ", PRICE[n] * Day[n], "\t")
                    print(" Restaurant Charges: \t", RC[n])
                    print(" --------------------------------")
                    print("\n Total Amount: ", (PRICE[n] * Day[n]) + RC[n], "\t")
                    print(" --------------------------------")
                    print("          Thank You")
                    print("          Visit Again :)")
                    print(" --------------------------------\n")
                    p.pop(n)
                    p.insert(n, 1)

                    # pops ROOM no. and customer id from list and
                    # later assigns zero at same position
                    ROOM_No.pop(n)
                    Customer_Id.pop(n)
                    ROOM_No.insert(n, 0)
                    Customer_Id.insert(n, 0)

            else:

                for j in range(n + 1, i):
                    if P_H == PHONE_No[j]:
                        if p[j] == 0:
                            pass

                        else:
                            f = 1
                            print("\n\tPayment has been made :)\n\n")
    if f == 0:
        print("Invalid Customer Id")

    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        sys.exit()
    return payment

# RECORD FUNCTION
def record():
    # checks if any record exists or not
    if PHONE_No:
        print("        *** HOTEL RECORD ***\n")
        print("| NAME        | PHONE No.    | ADDress       | Check-In  | Check-Out     | ROOM Type     | PRICE      |")
        print(
            "----------------------------------------------------------------------------------------------------------------------")

        for n in range(0, i):
            print("|", NAME[n], "\t |", PHONE_No[n], "\t|", ADD[n], "\t|", Checkin_Date[n], "\t|", Checkout_date[n], "\t|", ROOM[n],
                  "\t|", PRICE[n])

        print(
            "----------------------------------------------------------------------------------------------------------------------")

    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()

    else:
        sys.exit()
    return 0
# Driver Code
Home()

