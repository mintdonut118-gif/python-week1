fares={"Bangalore":950,"Chennai":500,"Hyderbad":788}
print(fares["Chennai"])
destination=input("enter the destination:")
if destination in fares:
    print(f"fare to destination{destination}is: {fares[destination]}")
else :
    print("Destination not found")