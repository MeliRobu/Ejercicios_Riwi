print("HI! Here you can ingress any product and update your inventory")
options=int(input("Type the number of iterations you want make: "))


for i in range (options):
   product_name=(input("\nType the product name: "))
   def price ():
       try:
           product_price= float(input("Type the product price: "))
           if product_price <0:
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


   print(f"\n\t***INVOICE*** \nThe product name is: {product_name} \nThe product amount is: {amount_variable} \nTge product price is: {price_variable} \nThe total amount is: {total_amount} ")