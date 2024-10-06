# # Programmers: Cody
# # Course: CS151, Professor Zee
# # Due Date: October 9th
# # Lab Assignment: PA1
# # Problem Statement: Write a program to make a story based off decisions inputted by the
##                      user
# # Data In: sport 1 position (position1_int) , sport selected (sport_str),
#   offense position (off_str), defensive position (def_str),
#   sport 2 position (position2_str), country selected (number2_int)
# # Data Out: name_str (Name of person), position, side of ball, country
# # Credits: None other than class

#The purpose of this program is to give positions/side of the field to user
# and the country if the user selected basketball

#Prompt the user for their name
name_str = str(input("Enter your name: "))

#Prompt the user to selected Football or Basketball
sport_str = str(input("Enter your sport, Football or Basketball: "))
sport_str = sport_str.lower()

#If user selects football
if sport_str == "football":
    position1 = float(input("Enter a number: 0-10: "))

    if position1 == 0:
        print(name_str, "is on special teams")
        stp_str = str(input("enter kicker or punter: "))
        stp_str = stp_str.lower()

        if stp_str == "kicker":
            print(name_str, "is a kicker")

        elif stp_str == "punter":
            print(name_str, "is a punter")

        else:
            print("Error, Try again.", name_str)

    elif 0 < position1  and position1 <= 6:
        print(name_str, "is on offense")
        off_str = str(input("enter quarterback, runningback, or widereceiver: "))
        off_str = off_str.lower()

        if off_str == "quarterback":
            print(name_str, "is a quarterback")

        elif off_str == "runningback":
            print(name_str, "is a runningback")

        elif off_str == "widereceiver":
            print(name_str, "is a widereceiver")

        else:
            print("Error, Try again.", name_str)

    elif 6 < position1 and position1 <= 10:
        print(name_str, "is on defense")
        def_str = str(input("enter linebacker, cornerback, or lineman: "))
        def_str = def_str.lower()

        if def_str == "linebacker":
            print(name_str, "is a linebacker")

        elif def_str == "cornerback":
            print(name_str, "is a cornerback")

        elif def_str == "lineman":
            print(name_str, "is a lineman")

        else:
            print("Error, Try again.", name_str)

    else:
        print("Error, Try again.", name_str)

#If user selects Basektball
elif sport_str == "basketball":
    position2_int = str(input("Enter pointguard, shootingguard, smallforward, "
                              "powerforward, or center: "))
    position2_int = position2_int.lower()

    if position2_int == "center":
        print(name_str, "is a center")

    elif position2_int == "pointguard":
        print(name_str, "is a pointguard")

    elif position2_int == "shootingguard":
        print(name_str, "is a shootingguard")

    elif position2_int == "smallforward":
        print(name_str, "is a smallforward")

    elif position2_int == "powerforward":
        print(name_str, "is a powerforward")

    else:
        print("Error, Try again.", name_str)

    #This will select the team they are on
    number2_int = int(input("Enter a number, 1, 2 or 3: "))

    if number2_int == 1:
        print(name_str, "is on Team USA")

    elif number2_int == 2:
        print(name_str, "is on China")

    elif number2_int == 3:
        print(name_str, "is on Russia")

    elif number2_int != 1 and number2_int != 2 and number2_int != 3:
        print("Error, Try again.", name_str)

else:
    print("Error, pick one of the sports above", name_str)









