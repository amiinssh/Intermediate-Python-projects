import math

print("Welcome to the online banking application")

name = ""
pin = ""
currentBalance = 0

def signIn():
    global name
    global pin
    global currentBalance
    
    name = input("Please enter a username: ")
    pin = input("Please create a 6-digit pin: ")
    
    if len(pin) == 6:
        print("Thanks for creating your bank account")
    else:
        print("Invalid pin. It has to be 6 digits")
        newPin = input("Please create a 6-digit pin: ")
        
        if len(newPin) != 6:
            print("The pin has to be 6 digits")
            signIn()
        else:
            pin = newPin    
    
def forgetPIN():
    global pin
    recoverpin = input("Please create a new 6-digit pin: ")
    
    if len(recoverpin) != 6:
        print("The PIN has to be 6 digits")
        forgetPIN()
    else:
        print("The new PIN has been stored, please log in")
        pin = recoverpin  
        logIn()
        
def depositInterests(p, r, t):
    p = float(p)
    r = float(r)
    t = float(t)
    return p * math.exp(r * t)

def logIn():
    global currentBalance
    
    name1 = input("Please enter your username: ")
    pin1 = input("Please enter your pin: ")
    
    if name1 == name and pin1 == pin:
        print(f"Welcome to the online banking system, {name}")
        print("Please choose the menu:")
        listMenu = [
            "1-Deposit", 
            "2-Withdraw", 
            "3-Transfer", 
            "4-Check Balance", 
            "5-Deposit Interest Rate", 
            "6-Calculate Compound Interest"
        ]
        
        for item in listMenu:
            print(item)
        
        userChoice = int(input("Please enter the number of desired service: "))
        
        if userChoice == 1:
            deposit = float(input("Enter the deposit amount: "))
            currentBalance += deposit
            print(f"Your current balance is: {currentBalance}")
        
        elif userChoice == 2:
            withdraw = float(input("Enter the amount of money you want to withdraw: "))
            
            if withdraw > currentBalance:
                print("Your account balance is not sufficient for this transaction")
            else:
                currentBalance -= withdraw
                print(f"{withdraw} has been withdrawn from your account. Your current balance is {currentBalance}")
        
        elif userChoice == 3:
            destination = input("Please enter the destination account number (8 digits): ")
            
            if len(destination) == 8:
                amount = float(input("Please enter the amount of money that you want to transfer: "))
                
                if amount > currentBalance:
                    print("Your account balance is not sufficient for this transaction")
                else:
                    currentBalance -= amount
                    print(f"The transaction of {amount} has been transferred to {destination}. Your current balance is {currentBalance}")
            else:
                print("The transaction was rejected since the destination was not valid")
        
        elif userChoice == 4:
            print(f"Your current balance is: {currentBalance}")
        
        elif userChoice == 5:
            if currentBalance > 50000:
                rate = 3
            elif currentBalance > 30000:
                rate = 2
            else:
                rate = 1.5
            print(f"Your current deposit interest rate is {rate}%")
        
        elif userChoice == 6:
            listOption = [
                "1-Calculate your deposit compound interest based on your current balance", 
                "2-Calculate your deposit compound interest based on your deposit input"
            ]
            
            for option in listOption:
                print(option)
            
            choice = int(input("Please enter your choice from the options above: "))
            
            if choice == 1:
                timing = float(input("How many years do you want to invest your money: "))
                if currentBalance > 50000:
                    ratex = 3 / 100
                elif currentBalance > 30000:
                    ratex = 2 / 100
                else:
                    ratex = 1.5 / 100
                
                print(f"Your balance after {timing} years will be: {depositInterests(currentBalance, ratex, timing)}")
            
            elif choice == 2:
                timing1 = float(input("How many years do you want to invest your money: "))
                money = float(input("Please enter the amount you wish to deposit: "))
                
                if money > 50000:
                    ratex = 3 / 100
                elif money > 30000:
                    ratex = 2 / 100
                else:
                    ratex = 1.5 / 100
                
                print(f"Your balance after {timing1} years will be: {depositInterests(money, ratex, timing1)}")
            else:
                print("Option is not available")
        else:
            print("Option is not available. Back to the main menu.")
    else:
        print("Your username or your PIN is wrong, did you create an account?")
        list1 = ["1-Yes", "2-No"]
        
        for item in list1:
            print(item)
        
        userResponse = int(input("Enter your choice below: "))
        
        if userResponse == 1:
            list2 = ["1-Do you want to log in again?", "2-You forgot your PIN"]
            for item in list2:
                print(item)
            
            theAnswer = int(input("Please enter your choice: "))
            
            if theAnswer == 1:
                logIn()
            elif theAnswer == 2:
                forgetPIN()
            else:
                print("Option is not available")
        elif userResponse == 2:
            print("Please create your account")
            signIn()
    app_exit()

def mainMenu():
    optionOne = int(input("Choose 1 to sign in and choose 2 to log in: "))
    
    if optionOne == 1:
        signIn()
    elif optionOne == 2:
        logIn()
    else:
        print("Option is not available")
        mainMenu()

def app_exit():
    answer = input("Do you still want to conduct transactions? Yes/No: ").lower()
    
    if answer == "yes":
        logIn()
    elif answer == "no":
        print("Thank you for using this app.")
    else:
        print("Option is not available")
        mainMenu()

# Start the program
mainMenu()
