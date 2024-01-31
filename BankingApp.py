
#Parent Class
class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print('Personal Details:')
        print("")
        print("Name: ", self.name)
        print('Age: ', self.age)
        print('Gender: ', self.gender)

    
class Bank(User):
    def __init__(self, name, age, gender,):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit (self, Amount):
        self.amount = Amount
        self.balance = self.balance + self.amount
        print(f'Amount Balance has been updated  : to {self.balance}')
    
    def withdraw(self,amount):
        self.amount = amount
        if (self.amount > self.balance):
            print(f'Insufficient funds! Balance Available \n Your Balance is {self.balance}')
        else:
            self.balance = self.balance - self.amount
            print(f"Account balance have been updated. Your account balance now is {self.balance}")
    
    def CalculateCharges(self, charges):
            self.charges = charges
            self.balance = self.balance - (self.balance * self.charges / 100)
    
    def view_balances(self):
        self.show_details()
        print(f'Yor Account balance is {self.balance} after a deduction of \n bank charge of  {self.balance * self.charges/100}')
        




















Joseph = Bank('Joseph', 45, 'Male')
Joseph.deposit(700)
Joseph.deposit(700)
print(Joseph.view_balances())
