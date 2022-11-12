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

information= {}

user_input = True

while user_input:
    if user== 1:
        print("Add an item")
        print("")    
        
        name=input("Full Name: ")
        age= int(input("Age: "))
        add=input("Address: ")
        phone= int(input("Phone Number: "))
        
        information={
            "name" : name,
            "age" :age,
            "add" : add,
            "phone" : phone

        }
        
        print("Saved!")


#Option 2

if user==2:
    print("Search")
    print("")

        
#Option 3
 