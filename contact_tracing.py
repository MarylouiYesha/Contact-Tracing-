#contact tracing

#menu

print("CONTACT TRACING")
print("")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")
print("")

#Option 1

user= int(input (" What do you want to do? (1-3)"))

if user== 1:
    print("Add an item")
    print("")

    name=input("Full Name: ")
    age= int(input("Age: "))
    add=input("Address: ")
    phone= int(input("Phone Number: "))

    info={
        "name_":{name},
        "age-":{age},
        "add_":{add},
        "phone_":{phone}
    }

    print("Saved!")


#Option 2

if user==2:
    print("Search")
    print("")

        
#Option 3
 