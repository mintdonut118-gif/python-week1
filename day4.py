
todo=[]
while True:
    print("1.add task 2.remove task 3.view task 4.quit")
    choice=input("enter the choice:")
    choice=int(choice)
    if choice==1:
         task=input("enter the task")
         todo.append(task)    
    elif choice==3:
       
     for i ,item in enumerate(todo,start=1):
          print(f"Task{i} {item}")
    elif choice==2:
      remove=input("which task to remove")
      if remove in todo:
        todo.remove(remove)
      else:
         print("taska not found")


    elif choice==4:
        print("quit")
        break

        
    

