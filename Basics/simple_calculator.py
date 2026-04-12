# type conversion is mandatory here. 
# Because every input we take via input() is considered to be str

First = int(input("First :"))
Second =  int(input("Second :"))

ans = First + Second
print("Sum :", ans)

#OR
First = input("First :")
Second =  input("Second :")

ans = float(First) + float(Second)
print("Sum :"+ str(ans))


