# fares={"Bangalore":950,"Chennai":500,"Hyderbad":788}
# print(fares["Chennai"])
# destination=input("enter the destination:")
# if destination in fares:
#     print(f"fare to destination{destination}is: {fares[destination]}")
# else :
#     print("Destination not found")
# sentence="the bus has left the depot"
# words=sentence.split()
# count={}
# for word in words:
#     if word in count:
#         count[word]=count[word]+1
#     else:
#         count[word]=1

# print(count)
todo=[]
while True:
    choice=input("1.add 2.view")
    choice=int(choice)
    if choice==1:
        item=input("enter the item")
        todo.append({"task": item, "done": False})
    elif choice==2:
        for i,item in enumerate(todo,start=1):
            mark = "x" if item["done"] else " "
            print(f"Task {i}: [{mark}] {item['task']}")
    elif choice==3:
        done=input("which task is done")
        done=int(done)
        n=int(done)-1
        todo[n]["done"]=True
    elif choice == 4:
     remove_num= input("which task to remove: ")
     remove_num = int(remove_num)
     n = remove_num - 1
     todo.pop(n)

           
