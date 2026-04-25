weight = int(input("Weight:"))
option = input("(K)g or (L)bs: ")

if option == "K" or option == "k":
    val = weight * 2.205
    print("weight in lbs: ", val )

elif option =="L" or option =="l":
    val2 = weight/2.205
    print("weight in kg: ", val2)

