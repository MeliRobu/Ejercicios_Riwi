#FUNTIONS INVENTORY
print("HI! Here you can ingress any product and update your inventory")
def product():
    product_name=(input("\no) Type the product name: "))
    if product_name.isdigit() or product_name =="" or product_name ==" ": 
        print("\nYou have to insert a product name, please try again.")
        return product()
    else:
        return product_name
name_product=product() 
def price ():
    try:
        product_price= float(input("o) Type the product price: "))
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
        product_amount= float(input("o) Type the product amount: "))
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

print(f"\n\t***INVOICE*** \n=>The product name is: {name_product} \n=>The product amount is: {amount_variable} \n=>The product price is: {price_variable} \n=>The total amount is: {total_amount} ")

another_product= input("\nDo you want to ingress another product? , type yes or no: ").lower()

while another_product == "yes":
    name_product=product() 
    amount_variable=amount()
    price_variable=price()
    total_amount= amount_variable*price_variable
    print(f"\n\t***INVOICE*** \n=>The product name is: {name_product} \n=>The product amount is: {amount_variable} \n=>The product price is: {price_variable} \n=>The total amount is: {total_amount} ")
    another_product= input("\nDo you want to ingress another product? , type yes or no: ")

print("\n\t***Process finished, have a nice day***")
  