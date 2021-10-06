#Build a Bus/Air/Rail Booking System where the user can choose a source and destination from the list given and enter the information passenger wise, depending on the distance cost shall be computed.
#Bus,Rail and Air systems will have different fares for different classes.You should be able to think of the system as how would he/she use it as a user.

mode=input("Hello! Welcome to the automated ticket system. Please enter a method how you would like to travel (Bus, Air or Rail): ").lower()
transport = {"bus":500,"air":4000,"rail":1500}
cost = 0
place = {"mumbai":1000,"hydrabad":900,"chennai":1200,"bangalore":950}
if mode=="bus" or mode=="air" or mode=="rail":
    print(f"You chose to travel by {mode.title()}")
    start=input(f"\n\nPlease select starting point from the following list:\nDelhi\nMumbai\nHydrabad\nChennai\nBangalore\nStaring Point: ").lower()
    cost+=transport[mode]
    if start=="mumbai" or start=="hydrabad" or start=="chennai" or start=="bangalore":
        print(f"You have set your starting point to {start.title()}")
    else:
        print("Please enter a valid starting point")
    destination=input(f"\nPlease select a destination from the following list\n(Please note that your destination can not be the same as your start point):\nDelhi\nMumbai\nHydrabad\nChennai\nBangalore\nDestination: ").lower()
    if destination==start:
        print("Your destination can not be the same as your starting point")
    elif destination=="delhi" or destination=="mumbai" or destination=="hydrabad" or destination=="chennai" or destination=="bangalore":
        print(f"You have set your destination to {destination}")
        cost+= place[destination]
        print(f"\n\nYou chose to travel by {mode}. From {start} to {destination} in {cost} rupees. Have a safe trip!")
    else:
        print("Please enter a valid destination")
        
else:
    print("Please enter a valid mode of transport")

