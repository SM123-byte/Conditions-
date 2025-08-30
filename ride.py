# Choose your ride 

print("Select your ride: \n 1. Bike \n 2. Car ")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("What type of bike?: \n 1. Sports Bike \n 2. Moped")
    choose = int(input("Enter your selection: "))
    if choose == 1:
        print("You have chosen a sports bike.")
    else:
        print("You have chosen a moped.")

elif choice == 2:
    print("What type of car?: \n 1. Sedan \n 2. SUV")
    choose2 = int(input("Enter your selection: "))
    if choose2 == 1:
        print("You have chosen a sedan.")
    else:
        print("You have chosen a SUV.")

else: 
    print("Wrong Choice!")

    