class Bankaccount:
  
  def __init__(self,account_number,account_holder_name,
initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
    
  def deposit(self,amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited {}.New balance:{}".format(amount,self.__account_balance))
    else:
      print("invalid deposit ,please deposit a positive amount.")
  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
        self.__account_balance -= amount
        print("withdraw {} . New balance: {}" .format( 
              amount,self.__account_balance))
    else:
        print("invalid withdrawal amount or insufficient balance.")
    def display_balance(self):
           print("account balance for{}(account #{}):{}".format(self.__account_holder_name,
          self.__account_number,
          self.__account_balance))

account=Bankaccount(account_number="12345678",account_holder_name="haripriya",initial_balance=5000.0)


#account.display_balance()
account.deposit(400.0)
account.withdraw(100)
account.display_balance()