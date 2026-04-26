#Colletions = one variable to store multiple values.
 
#List[] = ordered, mutable, duplicate ok
#Tuple() = ordered, immuable, duplicates ok
#set{} = unordered, immuable, no duplicates, add/remove element ok.
#dict{:,:} = ordered, mutable, no duplicates.

capitals = {"USA":"Washinton DC",
            "India":"New Delhi",
            "China":"beiging",
            "Russia":"Moscow"}
print(capitals)

print(capitals.get("China")) # for the Key returns its Value or none.

capitals.update({"Germany":"berlin"}) 
capitals.update({"USA":"Ohio"})
print(capitals)

# capitals.pop("China") #> remove the KV pair
# print( capitals)

# capitals.popitem() # removes the recent KV pair
# print(capitals)

# capitals.clear()
# print(capitals)

keys = capitals.keys();
print(keys)

values = capitals.values()
print(values)