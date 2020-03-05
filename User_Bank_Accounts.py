class user:	
    def __init__(self, name):
        self.name = name
        self.account_balance = BankAccount(0.10, 0)

class BankAccount:
	def __init__(self, int_rate, balance):
		self.int_rate = int_rate
		self.balance = balance
	
	def deposit(self, amount):
		self.balance += amount
		return self
	
	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
		else:
			print("Insufficient funds: Charging a $5 fee")
			self.balance -= 5
		return self
	
	def display_account_info(self):
		print(f"Balance: ${self.balance}")
		return self

	def yield_interest(self):
		if self.balance > 0:
			self.balance += self.balance * self.int_rate
		return self

user1 = user("Yong")
user1.account_balance.deposit(100).withdraw(200).yield_interest().display_account_info()

user2 = user("Eric")
user2.account_balance.deposit(1000).withdraw(2000).yield_interest().display_account_info()