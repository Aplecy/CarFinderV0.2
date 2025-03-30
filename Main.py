#ADDED SET OF ALLOWED VEHICLES
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

#create a defined option to call for the list then returns to menu
def Input1():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicles in AllowedVehiclesList:
        print (vehicles)
    print("")
    menu()
#create an defined option to exit the menu
def Input2():
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")

#create a search option for authorized vehicles
def Search():
    print("********************************")
    SEARCHvech = input("Please Enter the full Vehicle name: ")
    if SEARCHvech in AllowedVehiclesList:
        print(f"{SEARCHvech} is an authorized vehicle")
        menu()
    else:
        print(f"{SEARCHvech} is not an authorized vehicle, if you received this error please check the spelling and try again.")
        menu()

#create a defined menu for AutoCountry with options to show authorized vehicles and option to exit
def menu():
    print("********************************")
    print("AutoCountry Vehicle Finder V.01")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicles")
    print("3. Exit")
    option = int(input(""))
    if option == 1:
        Input1()
    elif option == 2:
        Search()
    elif option == 3:
        Input2()    

menu()