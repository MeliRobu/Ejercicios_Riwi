# ATM
# We have to ask to the client how many operations do he/she wanna do
# opcion 1. consultar saldo
balance = 1000
print("Hi! Welcome to the ATM ")
def login():
    try:
        user=input("Username: ")
        password=int(input("Password: "))
        if user == "meli123" and password ==1234:
            print("** Sucessful access **")
            return user, password
        else:
            print ("Denied access :( , please try again")
            return login()
    except ValueError:
        print("Denied access :( , please try again") 
        return login()
login()

def op ():
    try:
        op_n=int(input("How many transactions do you want to make ?: "))
        if op_n > 0:
            return op_n
        else:
            print("Invalid option, please try again")
            return op()
    except ValueError:
        print("Invalid option, please try again")
        return op()

    
def withdraw_money(): 
        try: 
            global balance
            amount= float(input("Type the amount of money to withdraw: "))
            if amount > balance :
                print("There is not enough amount of money")
                return withdraw_money()
            elif amount== 0 or amount < 0:
                print("The amount to withdraw can not be 0 or less than that, please try again.")
                return withdraw_money()
            elif amount <= balance:
                balance = balance - amount
                print(f"Succesful withdraw.  \nYour new balance is: {balance}")
                return amount
        except ValueError:
            print("Invalid option, please try again")
            return withdraw_money()
        
def deposit_money():
        try:         
            global balance
            deposit=  float(input("Type the amount of money that you want to deposit: "))
            if deposit > 0: 
                balance = balance+ deposit
                print(f"The new balance is: {balance} ")
                return deposit
            else:
                print(f"The amount to deposit can not be negative, please try again")
                return deposit_money()

        except ValueError:
            print("Invalid option, please try again")
            return deposit_money()
        
for i in range (op()):

    print("\n1.Consult your actual balance \n2.Withdraw money\n3.Deposit money\n4.Exit")
    atm_op=int(input("Please choose an option: "))

    if atm_op == 1:
        print(f"Your atual balance is {balance}")
    elif atm_op == 2: 
        withdraw_money()
    elif atm_op== 3:
        deposit_money()
    elif atm_op ==4:
        print("Thank you for using ATM, have a nice day")
        break
    else: 
        print("This option is invalid, please try again ")

    


    

