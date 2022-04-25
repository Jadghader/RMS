import tkinter as t
import os
from time import sleep
items = ("Lobster Bisque.","Baked Brie.","Clams with Vinegar & Shallots.","Calamari with Tomatoe Sauce.", "Crab bites with yogurt dressing.", "Shrimp Mango Salad.", "Greek Salad.", "Caesar Salad.", "Salmon and Avocado Salad.", "Nicoise Salad.", "Organic Salmon.", "Pan fried Cod.", "Pan Fried Sea Bass.", "Grilled lobster tails.", "Trout Mustard Risotto.", "Grapefruit Mint.", "Carrot Limeade.", "Minted Lemonade.", "Fruit Cockatail.", "Coke, Diet Coke, 7up, Miranda.", "Mango parfait with coconut sorbet.", "Chilled chocolate caramel fondant.","Lemon and Lavender Possets.","Chocolate Mousse.","Creme Brulee.")
prices = ((30,25,37,17,30),(20,24,43,17,40), (30, 22, 53, 21, 30), (25, 33, 70, 23, 25), (35, 23, 46, 20, 20))
places = [0]
for i in range(15):
    places += [0]
amount=[0]
for i in range(25):
    amount += [0]
itemtotal=[0]
for i in range(25):
    itemtotal += [0]
dailytotal = 0.0
totalamount = 0
reserved = 0
counter = 0
def login():
    global counter
    design()
    username = input("Username:")
    password = input("Password:")
    if username == "RMS" and password == "123":
        settings()
    elif counter < 3:
        print("Log in Falied, Try again")
        counter = counter + 1
        login()
    else:
        exit()
def settings():
    design2()
    print("1)Reservations\n\n2)Order From Menu\n\n3)Receipt History\n\n4)Total Sales\n\n5)End of Day\n\n6)Employee attendance")
    choice = int(input("Enter which window you would like to access:"))
    if choice == 1:
        seats()
    if choice == 2:
        order1()
    if choice == 3:
        history()
    if choice == 4:
        sales()
    if choice == 5:
        endofday()
    if choice == 6:
        employees()
def order1():
    global dailytotal
    global totalamount
    global itemtotal
    menu = open("Menu.txt","r")
    total = 0
    for m in menu:
        print(m)
    order = input("Enter your order(0-0 to return to main menu/6-6 for receipt):")
    ordertype, ordernb = order.split("-",1)
    ordertype = int(ordertype)
    ordernb = int(ordernb)
    while 0< ordertype <6 and 0<ordernb<6:
        r = open("Receipt.txt", "a+")
        h = open("History.txt", "a+")
        quantity = int(input("\nEnter quantity:"))
        price = (prices[ordernb - 1][ordertype - 1] * quantity)
        total = total + price
        dailytotal = dailytotal + float(total)
        x = 5 * (ordertype - 1) + (ordernb - 1)
        print("%d %s\n"% (quantity, items[x]))
        amount[x] = amount[x] + quantity
        totalamount = totalamount + amount[x]
        itemtotal[x] = itemtotal[x] + price
        string = str(quantity)+"%-40s\t$%5s\n"%(items[x],str(price))
        r.write(string)
        h.write(string)
        string2 = "%-40s\t$%5s\n"%("Total",str(total))
        r.close()
        h.close()
        order = input("Enter your order(0-0 to return to main menu/6-6 for receipt):")
        ordertype, ordernb = order.split("-", 1)
        ordertype = int(ordertype)
        ordernb = int(ordernb)
    if ordertype == 0 and ordernb == 0:
        r = open("Receipt.txt", "a+")
        h = open("History.txt", "a+")
        r.close()
        h.close()
        settings()
    if ordertype == 6 and ordernb == 6:
        if total == 0:
            print("You did'nt order yet")
            order1()
        else:
            r = open("Receipt.txt", "a+")
            h = open("History.txt", "a+")
            r.write(string2)
            h.write(string2)
            r.close()
            h.close()
            r = open("Receipt.txt", "r")
            h = open("History.txt", "r")
            for line in r:
                print(line)
            r.close()
            os.remove("Receipt.txt")
            h.close()
            ret = int(input("Enter 1 to return to main menu"))
            if ret == 1:
                settings()
    else:
        print("Invalid Syntax")
        order1()
def Printseats():
    for i in range(1, 16):
       print(" Table-%d :\t%3d "% (i, places[i]))
def seats():
    global reserved
    i = 0
    table = 0
    rsv = int(input("Enter 1 for reserving and 2 for unresrving "))
    if (rsv == 1):
            print("\n\nTABLE RESERVATION\n")
            print("-------------------\n")
            Printseats()
            print("Number of available tables: %d" % (15 - reserved))
            while (reserved != 15):
                seat = int(input("\nReserve a table?(table# / 0 = cancel)"))
                if seat in range(1,16) and places[seat]==0:
                    places[seat] = 1
                    print("\nYour table has been reserved!")
                    reserved = reserved + 1
                    Printseats()
                    print("Number of available tables: %d" % (15 - reserved))
                    seats()
                elif seat in range(1,16) and places[seat]!=0:
                    seat = int(input("\nTable is already taken,Reserve a table?(1 = yes/0 = cancel)"))
                if (seat == 0):
                    settings()
            print("\nWe are fully booked.")
            rsv = input("Enter 1 for mainmenu and 2 for unresrving ")
            if (rsv == 1):
                print("\nreturning to main menu...\n")
                settings()
            elif (rsv == 2):
                table = 0
                print("\n\nTABLE UNRESERVATION\n")
                print("-------------------\n")
                Printseats()
                table = int(input("\nEnter table no. to unreserve(0 = main menu):"))
                if table == 0:
                    settings()
                elif table in range(1, 16):
                    places[table] = 0
                    reserved= reserved - 1
                    Printseats()
                    seats()
    elif (rsv == 2):
        table = 0
        print("\n\nTABLE UNRESERVATION\n")
        print("-------------------\n")
        Printseats()
        table = int(input("\nEnter table no. to unreserve(0 = main menu):"))
        if table == 0:
            settings()
        elif table in range(1, 16) and places[table]==1:
            places[table] = 0
            reserved = reserved - 1
            Printseats()
            seats()
        elif places[table] == 0:
            print("Table already unreserved, returning to reservations mmenu")
            seats()
        else:
            print("Invalid, returning to main menu")
            settings()
def design():
    print("\t\t\t\t*****************************************************\n")
    print("\t\t\t\t***                                               ***\n")
    print("\t\t\t\t***                                               ***\n")
    print("\t\t\t\t***                                               ***\n")
    print("\t\t\t\t***                                               ***\n")
    print("\t\t\t\t***                                               ***\n")
    print("\t\t\t\t***            WElCOME TO OCEAN'S 25              ***\n")
    print("\t\t\t\t***         RESTAURANT MANAGEMENT SYSTEM          ***\n")
    print("\t\t\t\t***                                               ***\n")
    print("\t\t\t\t***                                               ***\n")
    print("\t\t\t\t***                                               ***\n")
    print("\t\t\t\t***                                               ***\n")
    print("\t\t\t\t*****************************************************\n")
    print("\n")
def design2():
    print("----------------------")
    print("\n  O C E A N ' S 25\n      Main Menu")
    print("\n----------------------\n")
def sales():
    print("%-40s\tQuantity\tTotal\n"% ("Items"))
    for i in range(25):
        print("%-40s\t%-6d\t\t$%-5d\n"% (items[i], amount[i], itemtotal[i]))
    print("----------------------------------------------------------------------------------\n")
    print("%-40s\t%-6d\t\t$%f"% ("Grand Total", totalamount, dailytotal))
    print("                                                        ==============")
    choice = int(input("\nEnter 1 to return to main menu"))
    if choice == 1:
        print("returning to main menu...")
        settings()
def history():
    h = open("History.txt","r")
    for i in h:
        print(i)
    h.close()
    choice1 = int(input("\nEnter 1 to return to main menu"))
    if (choice1 == 1):
        settings()
def endofday():
    frame = t.Tk()
    frame.title("End of Day")
    frame.geometry('400x200')
    def printInput():
        e3 = open("employee.txt", "r")
        e2 = open("temployee.txt", "w")
        os.remove("History.txt")
        e = open("EndOfDay.txt","w")
        string = input("Enter Date:")
        e.write(string+'\n')
        e2.write(string + '\n')
        for i in e3:
            e2.write(i)
        e.write("%-40s\tQuantity\tTotal\n" % ("Items"))
        for i in range(25):
            e.write("%-40s\t%-6d\t\t$%-5d\n" % (items[i], amount[i], itemtotal[i]))
        e.write("----------------------------------------------------------------------------------\n")
        e.write("%-40s\t%-6d\t\t$%f" % ("Grand Total", totalamount, dailytotal))
        e.write("                                                        ==============")
        e.close()
        e2.close()
        e3.close()
        os.remove("employee.txt")
    t.Label(frame, text='Chose one:').grid(row=0)
    endButton = t.Button(frame,text="End Of Day",command=printInput).grid(row=1,column=0)
    returnButton = t.Button(frame, text="Return", command=settings).grid(row=1, column=4)
    t.mainloop()
def employees():
    confirm = int(input("Press 1 to add employee, 0 to return to main menu"))
    emp={}
    if confirm == 0:
        settings()
    elif confirm == 1:
        e = open("employee.txt","a+")
        key = input("Enter employee's ID")
        value = input("Enter Time of arrival")
        emp[key]=value
        e.write("ID:"+"%-10s"%(key)+"\tTime of arrival:"+"%-6s"%(emp[key])+"\n")
        e.close()
        employees()
    else:
        print("Invalid syntax")
        employees()
login()
settings()
