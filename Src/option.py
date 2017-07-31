################################## File Description ######################################
## Author: Aureliano Yepez 																##
## Date: July 22, 2017																	##
## option.py allows users to chose whether s/he wants to budget, or just 				##
## see his or her total monthly,weekly, and or daily spendingd							##
##########################################################################################
def checkIfBudget(response):
	if (response == ("Y" or "Yes" or "yes" or "YES")): 
		print("You are simulating a budgeting")
		#Should call a function
	else:
		print("You are not simulating budget")
		#Should call another function 