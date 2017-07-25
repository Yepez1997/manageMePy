## File Description ## 
## Author: Aureliano Yepez 
## Date: July 22, 2017
### Create an excel sheet out of this ? 


## Uses dictionary to store data 
## {Key=Item, Value=Cost} *Items should update/ increment if same 
class Items:
	### Totals ###
	taxes = .925 # check for taxes for areas
	totalItems = 0 
	totalCost = 0 
	listItems = {}
	###  Groceries ###
	totalItemsGroceries = 0 
	costGroceris = 0
	listGroceries = {}
	### Personal ###
	totalItemsPersonal = 0 
	costPersonal = 0 
	listPersonal = {}
	### Housing ###
	totalItemsHousing = 0
	costHousing = 0 
	listHousing = {}
	### School ###
	totalSchoolItems = 0 
	costSchoolItems = 0
	listSchoolItems = {}
	### Custom ###
	totalItemsCustom = 0
	totalCustom = 0 
	listCustom = {}


	
	## Groceries method should update item, cost, 
	## Should get the timestamp - current day and time inputed 
	def groceries(self, item , cost, quantity): #cost is individual item
		self.listGroceries[item] = cost
		print("You have added: " + item  + "to your list of groceries") 
		print("The total amount of groceries in your list:")
		totalItemsGroceries += quantity
		groceriesList()

		
	def groceriesList(self):
		for item in listGroceries:
			for cost in listGroceries:
				print("Your current list: ")
				print(item, quantity, quantity * cost) 




	# Purpose of this function is to check whether the individual 
	# is able to purchase the item 
	#def checkGroceriePurchase(self):

#**************** Calls to construct class lists ***************#
# Should be user interface 
# Asks about the type of lists and what to add 
# Should know whether the item is in the list 



