################################## File Description ######################################
## Author: Aureliano Yepez 																##
## Date: July 22, 2017																	##
## items.py is a list of classes that contain potential categories for the user to input##
## his or her items into   																##
##########################################################################################

# class TrackInstances()
# 	instances = []
# 	def __init__(self, foo):
#         self.foo = foo
#         TrackInstances.instances.append(self)

## Uses dictionary to store data 
## {Key=Item, Value=Cost} *Items should update/ increment if same 

import datetime

class Items:

	## list___ are dictionaries
	### Totals ###
	taxes = .925 # check for taxes for areas
	
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
	## only for groceries for now 
	def __init__(self, item , cost, quantity): #cost is individual item
		self.item = item 
		self.cost = cost 
		self.quantity = quantity

#***** Grocery Class *****#
class Grocery(Items):
	def __init__(self,item,cost,quantity):
		Items.__init__(self, item, cost, quantity)
		
		#groceryAdd(self,item,cost,quantity)
		##More Categories sooner *"beta categories"
	def groceryAdd(self, item, cost, quantity): ## remember i added datetime 
		self.datetime = datetime.datetime
		self.listGroceries[item] = cost
		print("You have added: " + str(quantity) + " " + item +"(s)"  + " to your list of groceries") 
		Items.totalItemsGroceries += quantity
		print("The total amount of groceries in your list: ") 
		return Items.totalItemsGroceries
		
			
	def gList(self): #gList == groceriesList
		print("Your current list: ")
		for key in self.listGroceries: # i goes through keys 
				print(key, self.listGroceries[key])
		print("-----Current------")
		print("Item", "Quantity","Total Cost")
		return self.item, self.quantity, self.quantity * self.cost

#***** School Class *****#
class School(Items):
	def __init__(self,item,cost,quantity):
		Items.__init__(self,item,cost,quantity)

	def schoolAdd(self,item,cost,quantity,datetime):
		self.datetime = datetime.datetime
		self.listSchool[item] = cost 
		print("You have added: " + str(quantity) + " " + item +  "(s)" + " to your list of school items")
		Items.totalSchoolItems += quantity
		print("The total amount of school items in your list: ")
		return Items.totalSchoolItems

	def sList(self):
		print("Your current list: ")
		for key in self.listSchool:
			print(key, self.listSchool[key])
		print("-----Current-----")
		print("Item", "Quantity","Total Cost")
		return self.item, self.quantity, self.quantity * self.cost

#***** Personal Class *****#
class Personal(Items):
	def __init__(self,item,cost,quantity):
		Items.__init__(self,item,cost,quantity)

	def personalAdd(self,item,cost,quantity,datetime):
		self.datetime = datetime.datetime
		self.listPersonal[item] = cost 
		print("You have added: " + str(quantity) + " " + item +  "(s)" + " to your list of school items")
		Items.totalItemsPersonal += quantity
		print("The total amount of school items in your list: ")
		return Items.totalItemsPersonal

	def pList(self):
		print("Your current list: ")
		for key in self.listPersonal:
			print(key, self.listPersonal[key])
		print("-----Current-----")
		print("Item", "Quantity","Total Cost")
		return self.item, self.quantity, self.quantity * self.cost

#***** Housing Class *****#
class Housing(Items):
	def __init__(self,item,cost,quantity):
		Items.__init__(self,item,cost,quantity)

	def housingAdd(self,item,cost,quantity, datetime):
		self.datetime = datetime.datetime
		self.listHousing[item] = cost 
		print("You have added: " + str(quantity) + " " + item + "(s)" + " to your list of school items")
		Items.totalItemsHousing += quantity
		print("The total amount of school items in your list: ")
		return Items.totalItemsHousing

	def hList(self):
		print("Your current list: ")
		for key in self.listHousing:
			print(key, self.listHousing[key])
		print("-----Current-----")
		print("Item", "Quantity","Total Cost")
		return self.item, self.quantity, self.quantity * self.cost

#***** Custom Class *****#
class Custom(Items):
	def __init__(self,item,cost,quantity):
		Items.__init__(self,item,cost,quantity)

	def customAdd(self,item,cost,quantity,datetime):
		self.datetime = datetime.datetime
		self.listCustom[item] = cost 
		print("You have added: " + str(quantity) + " " + item + "(s)" + " to your list of school items")
		Items.totalItemsCustom += quantity
		print("The total amount of school items in your list: ")
		return Items.totalItemsCustom

	def cList(self):
		print("Your current list: ")
		for key in self.listCustom:
			print(key, self.listCustom[key])
		print("-----Current-----")
		print("Item", "Quantity","Total Cost")
		return self.item, self.quantity, self.quantity * self.cost


	# Purpose of this function is to check whether the individual 
	# is able to purchase the item 
	#def checkGroceriePurchase(self):

## Class totals prints out every created class 
## Every created class is stored in a dictionary
## Totals inherits the Class Items, which contains the  

##### August 3rd: this class needs tweeking -- trying to get to work with adding stuff in first 
"""
class Totals(Items)
	totalsCost = [] #use sum(to print total sum of everything)
	totalItems = [] #use for loop to count every item in the list 

	def __init__(self):
		Items.__init__(self):

	def groceriesIter(self):
		print('########## Groceries List ##########')
		print()

	def housingIter(self):
		print('########## Housing List ##########')
		hList()

	def personalIter(self):
		print('########## Personal List ##########')	
		pList()

	def schoolIter(self):
		print('########## School List ##########')
		sList()

	def customIter(self):
		print('########## Custom List ##########')
		cList()

	def Totals(self):
		print('Total Cost: ' + str(sum(totalsCost)) 
		print('Total Items: ' + str(len(totalItems))) 
"""


#**************** Calls to construct class lists ***************#
# Should be user interface 
# Asks about the type of lists and what to add 
# Should know whether the item is in the list 

### Test Cases ###
## Create a list that automatically generates
## Use while loop 
## Maybe implement the Ratcliff and Obershelp




