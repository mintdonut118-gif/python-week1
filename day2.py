# for number in range (1 ,51):

#   if  number%5==0 and number%3==0:
#     print("fizzbuzz")
#   elif number%5==0:
#     print("buzz")
#   elif number%3==0:
#     print("fizz")
#   else :
#     print(number)
# number=10
# number=int(number)
# while number>0:
#  print(number)
#  number=number-1
#  if number==4:
#     break
# marks=[90,55,44,32,33]
# for i,mark in enumerate(marks,start=1):
#         print(f"Subject{i}:{mark}")
# realpin="4321"
# attempt=0
# while attempt<4:
#     pin=input("enter the pin:  ")
#     if pin==realpin:
#        print("Pin is right")
#        break
#     else:
#      print("try again")
#     attempt=attempt+1
# else:
#      print("card locked") 
import random
secret=random.randint(1,100)
while True:
 number=input("enter the number")
 number=int(number)
 if(number>secret):
   print("lower")
 elif(number<secret):
  print("higher")
 else:
  print("right  ans")
  break
