class BankAccount:
  def init(self, account_number, holder_name, balance=0):
      self.account_number = account_number
      self.holder_name = holder_name
      self.balance = balance

  def deposit(self, amount):
      if amount > 0:
          self.balance += amount
          print(f"Deposited ${amount}. New balance: ${self.balance}")
      else:
          print("Invalid deposit amount.")

  def withdraw(self, amount):
      if 0 < amount <= self.balance:
          self.balance -= amount
          print(f"Withdrew ${amount}. New balance: ${self.balance}")
      else:
          print("Invalid withdrawal amount or insufficient balance.")

  def get_balance(self):
      return self.balance

  def transfer(self, other_account, amount):
      if amount <= self.balance:
          self.balance -= amount
          other_account.deposit(amount)
          print(f"Transferred ${amount} to {other_account.holder_name}")
      else:
          print("Insufficient balance for the transfer.")

def main():
  accounts = {}

  while True:
      print("\nBanking System Menu:")
      print("1. Create Account")
      print("2. Deposit")
      print("3. Withdraw")
      print("4. Check Balance")
      print("5. Transfer Funds")
      print("6. Exit")

      choice = input("Enter your choice: ")

      if choice == '1':
          account_number = input("Enter account number: ")
          holder_name = input("Enter account holder name: ")
          new_account = BankAccount(account_number, holder_name)
          accounts[account_number] = new_account
          print("Account created successfully.")
      elif choice == '2':
          account_number = input("Enter account number: ")
          if account_number in accounts:
              amount = float(input("Enter deposit amount: $"))
              accounts[account_number].deposit(amount)
          else:
              print("Account not found.")
      elif choice == '3':
          account_number = input("Enter account number: ")
          if account_number in accounts:
              amount = float(input("Enter withdrawal amount: $"))
              accounts[account_number].withdraw(amount)
          else:
              print("Account not found.")
      elif choice == '4':
          account_number = input("Enter account number: ")
          if account_number in accounts:
              balance = accounts[account_number].get_balance()
              print(f"Account balance for {accounts[account_number].holder_name}: ${balance}")
          else:
              print("Account not found.")
      elif choice == '5':
          account_number1 = input("Enter your account number: ")
          account_number2 = input("Enter recipient's account number: ")
          if account_number1 in accounts and account_number2 in accounts:
              amount = float(input("Enter transfer amount: $"))
              accounts[account_number1].transfer(accounts[account_number2], amount)
          else:
              print("One or both accounts not found.")
      elif choice == '6':
          print("Thank you for using the Banking System. Goodbye!")
          break
      else:
          print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
  main()