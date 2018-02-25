## File Description ##
## Author: Aureliano Yepez
## Date: July 22, 2017
"""
Parse purchases from banks ? First complete what is needed ! 

"""

class Account:

	numberWithdraws = 0
	numberDeposits =  0
	interest = 0.2 # will not be used for now ...
	hasBank = True
	isValidBank =  False
	country =" United States"
	#not all the banks -- few major ones
	banks = ["chase","bank of america", "wells fargo","citi bank","goldman sachs","morgan stanley",
			"bancorp", "capitol one"]

	def __init__(self,name,bank):
		self.name = name
		# if self.bank in banks:
		self.bank = bank
		self.balance = 0


	def withdraw(self, amount):

		self.balance = self.balance - amount
		if (self.balance > 0):
			print("Your current amount is: " + str(self.balance))
		else:
			raise AssertionError("Not enough money to withdraw")
		Account.numberWithdraws +=  1


	def deposit(self, amount):
		self.balance = self.balance + amount
		print("Your current amount is: " + str(self.balance))
		Account.numberDeposits += 1
