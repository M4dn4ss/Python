accountSamed = {
    "name" : "Samed",
    "accountNo": "13345678",
    "balance": 3000,
    "additionalAccount": 2000
}

accountAli = {
    "name" : "Ali",
    "accountNo": "12345678",
    "balance": 2000,
    "additionalAccount": 1000
}

def withdrawMoney(account, amount):
    print(f'Hello {account["name"]}')

    if (account['balance'] >= amount):
        account["balance"] -= amount
        print('You can take your money.')
        learnBalance(account)
    else:
        sum = account["balance"] + account["additionalAccount"]

        if (sum >= amount):
            additionalAccountUsage = input("Do you want to use the additional account? (e/h)")

            if additionalAccountUsage == 'e':               

                additionalAccountUsageAmount = amount - account["balance"]
                account["balance"] = 0
                account["additionalAccount"] -= additionalAccountUsageAmount                                    

                print("You can take your money.")
                learnBalance(account)
            else:
                print(f'{account["accountNo"]}. account has {account["balance"]} balance.')
        else:
            print("We are sorry.You have insufficent balance.")
            learnBalance(account)

def learnBalance(account):
    print(f'Account number {account["accountNo"]} has {account["balance"]} funds. Your additional account limit is {account["additionalAccount"]}.')


withdrawMoney(accountSamed, 3000)

withdrawMoney(accountSamed, 2000)
