# name=input("enter your name: ")
# words=name.split()
# result=""
# for word in words:
#    result=result+word[0].upper()+"."
# print(result)
# name=input("enter the name to reverse")
# result=name[::-1]
# print(result)
# if name==result:
#  print("palindrom")
# else:
#    print("not palindrom")
# name=input("enter the vowel check: ")
# count=0
# for letter in name:
#     if letter in "aeiou":
#      count=count+1
# print(f"vowel count:{count}")
price=input("enter the price")
price=price.replace("₹","")
price=price.replace(",","")
price=price.strip()
price=int(price)
gst=price * 1.18
print(f"base price{price} and new gst price{ gst:.2f}")