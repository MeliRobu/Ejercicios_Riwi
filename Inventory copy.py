#FUNTIONS INVENTORY
print("HI! Here you can ingress any product and update your inventory")
def product():
    product_name=(input("\nType the product name: "))
    if product_name.isdigit() or product_name =="" or product_name ==" ":
        print("\nYou have to insert a product name, please try again.")
        return product()
    else:
        return product_name
name_product=product()
def price ():
    try:
        product_price= float(input("Type the product price: "))
        if product_price <=0:
            print("The price cannot be negative")
            return price()
        else:
            return product_price
    except ValueError:
        print("Please type a number")
        return price()
def amount():
    try:
        product_amount= float(input("Type the product amount: "))
        if product_amount <0:
            print("The price cannot be negative")
            return amount()
        return product_amount
    except ValueError:
        print("Please type a number")
        return amount()
amount_variable=amount()
price_variable=price()
total_amount= amount_variable*price_variable

def dictionary():
    name = name_product
    price = price_variable
    amount = amount_variable
    total= total_amount
    return {
        "nombre":name,
        "precio":price,
        "cantidad":amount,
        "total": total
    }
Lista_producto = []
Lista_producto.append(dictionary())



print(f"\n\t***INVOICE*** \nThe product name is: {name_product} \nThe product amount is: {amount_variable} \nTge product price is: {price_variable} \nThe total amount is: {total_amount} ")


another_product= input("Do you want to ingress another product? , type yes or no: ")


while another_product== "yes":
    name_product=product()
    amount_variable=amount()
    price_variable=price()
    total_amount= amount_variable*price_variable
    Lista_producto.append(dictionary())
    print(f"\n\t***INVOICE*** \nThe product name is: {name_product} \nThe product amount is: {amount_variable} \nTge product price is: {price_variable} \nThe total amount is: {total_amount} ")
    another_product= input("Do you want to ingress another product? , type yes or no: ")
    


    if another_product== "no":
        print("\n\t***Process finished, have a nice day***")
        break

print(Lista_producto)