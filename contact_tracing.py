#contact tracing

#menu

print("CONTACT TRACING")
print("")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")
print("")



user= int(input (" What do you want to do? (1-3)"))

information= {}


#Option 1

if user== 1:
    print("Add an item")
    print("")    
        
    for i in range(10):
        name=input("Full Name: ")
        age= int(input("Age: "))
        add=input("Address: ")
        phone= int(input("Phone Number: "))
        
        information.update({name: age})
        information.update({add: phone})

    print(information)

#Option 2
    if user==2:
        print("Search")
        print("")
        



        
#Option 3
 