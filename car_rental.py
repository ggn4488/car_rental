import os

# Initializes lists
available = ["Chevrolet Tracker", "Chevrolet Onix", "Chevrolet Spin", "Hyundai HB20", "Hyundai Tucson", "Fiat Uno", "Fiat Mobi", "Fiat Pulse"]          
price_available = [120, 90, 150, 85, 120, 60, 70, 130]
unavailable = []
price_unavailable = []

# Shows catalog
def show_catalog():
    for i in range(len(available)):
        print("[{}] {} - R$ {} /day".format(i, available[i], price_available[i]))

# Rents
def rent(available, price_available, unavailable, price_unavailable):
    print("Type the number of the car you want to rent.")
    car_code = int(input())
    print("Type the number of days for which you want to rent.")
    n_days = int(input())
    print("You chose {} for {} days. Do you want to proceed?".format(available[car_code], n_days))
    print("That would cost R$ {}. Do you wish to rent? 1 - Yes, 0 - No".format(price_available[car_code]*n_days))
    rent = int(input())
    if rent == 1:
        print("Congratulations. You've rented {} for {} days.".format(available[car_code], n_days))
        unavailable.append(available[car_code])
        price_unavailable.append(price_available[car_code])
        del available[car_code]
        del price_available[car_code]
    print("1 - Go back | 0 - Leave program")
    go_leave = int(input())
    if go_leave == 1:
        return(available, price_available, unavailable, price_unavailable)
    else:
        os._exit(0)
    

# Returns
def returning(available, price_available, unavailable, price_unavailable):
    print("Here's the list of rented cars.")
    for i in range(len(unavailable)):
        print("[{}] {} - R$ {} /day".format(i, unavailable[i], price_unavailable[i]))
    print("Type the code of the car you want to return.")
    car_code = int(input())
    print("Thank you for returning {}".format(unavailable[car_code]))
    available.append(unavailable[car_code])
    price_available.append(price_unavailable[car_code])
    del unavailable[car_code]
    del price_unavailable[car_code]
    print("1 - Go back | 0 - Leave program")
    go_leave = int(input())
    if go_leave == 1:
        return(available, price_available, unavailable, price_unavailable)
    else:
        os._exit(0)

while True:
    print("Welcome to our car rental services")
    print("==================================")
    print("What do you wish to do?")
    print("0 - Show catalog | 1 - Rent a car | 2 - Return a car | 3 - Leave program")
    wish = int(input())
    if wish == 0:
        os.system("cls")
        show_catalog()
    elif wish == 1:
        available, price_available, unavailable, price_unavailable = rent(available, price_available, unavailable, price_unavailable)
    elif wish == 2:
        os.system("cls")
        available, price_available, unavailable, price_unavailabel = returning(available, price_available, unavailable, price_unavailable)
    else:
        os._exit(0)