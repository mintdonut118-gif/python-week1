# name=input("enter your name: ")
# words=name.split()
# result=""
# for word in words:
#    result=result+word[0].upper()+"."
# print(result)
name=input("enter the name to reverse")
result=name[::-1]
print(result)
if name==result:
 print("palindrom")
else:
   print("not palindrom")
       