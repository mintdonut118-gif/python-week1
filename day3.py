# def greet(name):
#     print(f"hello {name}")

# greet("sai")
# def gst(amount,rate=10):
#     return amount*(1+rate/100)
# # print(gst(2500))
# print(gst(3000,5))
# print(gst(3000)+5)
# def palindrome(word):
#     word=word.lower().replace(" ","")
#     return word==word[::-1]
# print(palindrome("madam"))
# def discount(price,discount):
#     if discount<0 or discount>100:
#         print("invalid")
#         return price
#     return  price*(1-discount/100)
# print(discount(500,10))
import random
def guess():
    number=input("enter the number")
    number=int(number)
    return number
def checkguess(guess, secret):
    if guess>secret:
        return "higher" 
    elif guess<secret:
        return "lower"
    elif guess==secret:
        return "same"
def guessgame():
   secret=random.randint(0,100)
   attempts=0
   while True:
    g=guess()
    result=checkguess(g,secret)
    print(result)
    attempts=attempts+1
    if result=="same":
     print(f"took {attempts} attempts")
     break

guessgame()