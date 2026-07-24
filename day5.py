# fares={"Bangalore":950,"Chennai":500,"Hyderbad":788}
# print(fares["Chennai"])
# destination=input("enter the destination:")
# if destination in fares:
#     print(f"fare to destination{destination}is: {fares[destination]}")
# else :
#     print("Destination not found")
sentence="the bus has left the depot"
words=sentence.split()
count={}
for word in words:
    if word in count:
        count[word]=count[word]+1
    else:
        count[word]=1

print(count)