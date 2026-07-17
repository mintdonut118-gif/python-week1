name=input("enter your name: ")
words=name.split()
result=""
for word in words:
    result=result+word[0].upper()+"."
print(result)