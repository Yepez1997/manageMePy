## File Description ## 
## Author: Aureliano Yepez 
## Date: July 22, 2017
### Create an excel sheet out of this ? 
from .main import Account 

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
	def groceries(self, item):
		self.listGroceries.append(item)
		totalCost

	# Purpose of this function is to check whether the individual 
	# is able to purchase the item 
	def checkGroceriePurchase(self):



