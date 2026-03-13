#ICE CREAM PARLOR
print("\tHi welcome to the ICE CREAM PARLOR")

"""
for o in range (5):
    flavor=input("\nWhich flavor of ice cream do you want: vainila, chocolate or strawberry?: ")

flavor_list= []
flavor_list.append(flavor)
print(flavor_list)

"""
s= 0
c= 0
v= 0
for o in range (5):
    def f():
        try:
            flavor=input("\nWhich flavor of ice cream do you want: vainila, chocolate or strawberry?: ")
            if flavor == "strawberry":
                s+=1
            elif flavor == "chocolate":
                c+=1
            elif flavor == "vainila":
                v +=1
            elif flavor != "strawberry" or flavor != "chocolate" or flavor != "vainila":
                print("Incorrect choice, please try again")
                return f()
            elif flavor.isdigit() or flavor.isspace():
                print("Incorrect choice, please try again")
                return f()
        except ValueError:
            print("Incorrect choice, please try again")
            return f()
print 

    