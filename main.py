# Non OOP
# Bank Version 1
# Single Account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'
i = 3
def balance():
    return str(accountBalance)
def deposit(amount):
    global accountBalance
    accountBalance += amount
    return("deposited " + str(amount) + " into your account.")
def withdrawl(amount):
    global accountBalance
    accountBalance -= amount
    return("withdrew " + str(amount) + " from your account.")
def show():
    global accountName 
    global accountBalance 
    global accountPassword
    print(f"Account name: {accountName}\nAccount Balance: {accountBalance}\nAccount password: {accountPassword}")
def instructions():
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawl')
    print('Press s to show the account')    
    print('Press q to quit')
while i > 0:
    userPassword = input('Please enter your password: ')
    jj = True
    while userPassword == accountPassword:
        if jj == True:
            instructions()
        jj = False
        action = input("What do you want to do? ")
        action = action.lower()
        action = action[0]
        if action == 'b':
            print(balance())
        elif action == 'd':
            print(deposit(int(input("How much would you like to deposit?"))))
        elif action == 'w':
            print(withdrawl(int(input("How much would you like to withdrawl?"))))
        elif action == 's':
            show()
        elif action == 'q':
            exit()
        else:
            print("Enter a valid action")
            instructions()
    i = i-1
    print(f"Incorrect password. {i} attempts left.")
print("Too many failed attempts. Terminating your family.")
exit()

        