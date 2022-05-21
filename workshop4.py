class User:
  def __init__(self, name, pin, password):
    self.name = name
    self.pin = pin
    self.password = password

  def change_name(self, name):
    name = str(name)
    self.name = str(self.name)
    if len(name) <= 2 or len(name) >= 10:
        print("Name length must be greater than 2 and lesser than 10 characters")
    elif name == self.name:
        print("New username cannot be the same as the previous value")
    else:
        self.name = name
        return name

  def change_pin(self, pin):
    pin = str(pin)
    self.pin = str(self.pin)
    if len(pin) != 4:
        print("Pin length must be exactly 4 numbers")
    elif pin.isdigit() == False:
        print("No strings allowed in pin")
    elif pin == self.pin:
        print("New pin cannot be the same as the previous value")
    else:
        self.pin =pin
        return pin

  def change_password(self, password):
    password = str(password)
    if len(password) < 5:
        print("Password length must at least 5 characters")
    else:
        self.password = password
        return password
 
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.name = name
        self.pin = pin
        self.password = password
        self.balance  = 0
        self.onhold = False

    def on_hold(self):
        if self.onhold is False:
            print("You put the account on Hold")
            self.onhold = True
            return self.onhold

    def show_balance(self):
        print(self.name,  "has an balance of", "${:,.2f}".format(self.balance))

    def withdraw(self, withdraw):
        if self.onhold == True:
            print("This account is on hold. Please try again later")
        elif type(withdraw) == str or withdraw < 0:
            print("Invalid input. You cannot input strings or negative numbers")
        else:
            float(withdraw)
            new_withdraw = self.balance - withdraw
            print(self.name,  "has an balance of", "${:,.2f}".format(new_withdraw))
            self.balance = new_withdraw
            return self.balance

    def deposit(self, deposit):
        if self.onhold == True:
            print("This account is on hold. Please try again later")
        elif type(deposit) == str or deposit < 0:
            print("Invalid input. You cannot input strings or negative numbers")
        else:
            float(deposit)
            new_balance = self.balance + deposit
            print(self.name,  "has an balance of", "${:,.2f}".format(new_balance))
            self.balance = new_balance
            return self.balance

    def transfer_money(self, user):
        while True:
            if self.onhold == True:
                print("This account is on hold. Please try again later")
                return
            else:
                try:
                    transfer_amt = float(input("How much would you like to transfer to " + user.name + "? $"))
                except:
                    print("Invalid amount. Please try again")
                    continue

                if transfer_amt <= self.balance and transfer_amt > 0:
                    print("you are transfering to: ", user.name)
                    user_pin = input("Enter your pin: ")
                    user_pin = int(user_pin)
                    if user_pin == self.pin:
                        print("Transfer authoried")
                        print("transfering", transfer_amt, "to", user.name)
                        self.balance = self.balance - transfer_amt
                        user.balance = user.balance + transfer_amt
                        self_converted = "${:,.2f}".format(self.balance)
                        user_converted = "${:,.2f}".format(user.balance)
                        print(self.name, "has an account balance of", self_converted)
                        print(user.name, "has an account balance of", user_converted)
                        return self.balance, user.balance
                    else:
                        print("Invalid pin")

                elif transfer_amt > self.balance:
                    print("You have insufficient funds in you account for transfer")

                elif transfer_amt <= 0:
                    print("Transfer amount must be greater than $0")  

                elif user_pin != self.pin:
                    print("Invalid pin")

    def request_money(self, user):
        while True:
            if user.onhold == True:
                print("This account is on hold. Please try again later")
                return
            else:
                try:
                    request_amt = float(input("How much would you like to request from " + user.name + "? $"))
                except:
                    print("Invalid amount. Please try again")
                    continue
                if request_amt <= user.balance and request_amt > 0:
                    print("you are requesting money from: ", user.name)
                    print("Transfer authoried")
                    print("Requestiong", "${:,.2f}".format(request_amt), "from", user.name)
                    routing_pin = input("Enter your pin: ")
                    routing_pin = int(routing_pin)
                    if routing_pin == user.pin:
                        self.balance = self.balance + request_amt
                        user.balance = user.balance - request_amt
                        self_converted = "${:,.2f}".format(self.balance)
                        user_converted = "${:,.2f}".format(user.balance)
                        print(self.name, "has an account balance of", self_converted)
                        print(user.name, "has an account balance of", user_converted)
                        return self.balance, user.balance
                    else:
                        print("Invalid pin")

                elif request_amt > user.balance:
                    print(user.name, "does not have enough funds for this request")

                elif request_amt <= 0:
                    print("Request amount must be greater than $0")

                elif routing_pin != self.pin:
                    print("Invalid pin")
    

""" Driver Code for Task 1 """
person = User("Bob", 1234, "password")
print(person.name, person.pin, person.password)

""" Driver Code for Task 2 """
person = User("Bob", 1234, "password")
print(person.name, person.pin, person.password)
person.change_name("Bobby")
person.change_pin(4321)
person.change_password("newpassword")
print(person.name, person.pin, person.password)

""" Driver Code for Task 3"""
new_person = BankUser("Bob", 1234, "password")
print(new_person.name, new_person.pin, new_person.password, new_person.balance)

""" Driver Code for Task 4"""
new_person = BankUser("Bob", 1234, "password")
new_person.show_balance()
new_person.deposit(1000)
new_person.withdraw(100)


""" Driver Code for Task 5"""
new_person = BankUser("Bob", 1234, "password")
new_person2 = BankUser("Alice", 1111, "password1")

""" Commenmt below 2 lines of code to unlock the account and permit all activities """
# new_person.on_hold()
# new_person2.on_hold()

""" Driver Code for Task 5"""
new_person.show_balance()
new_person.deposit(1000.11)
new_person2.deposit(5000.11)
new_person.withdraw(1000.11)
new_person2.withdraw(5000.11)
new_person.deposit(1000.10)
new_person2.deposit(5000)

new_person.transfer_money(new_person2)
new_person.request_money(new_person2)