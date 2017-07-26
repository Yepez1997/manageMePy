## File Description ## 
## Author: Aureliano Yepez 
## Date: July 22, 2017
### Create an excel sheet out of this ? 

# class TrackInstances()
# 	instances = []
# 	def __init__(self, foo):
#         self.foo = foo
#         TrackInstances.instances.append(self)

## Uses dictionary to store data 
## {Key=Item, Value=Cost} *Items should update/ increment if same 
class Items:
	## list___ are dictionaries
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
	## only for groceries for now 
	def __init__(self, item , cost, quantity): #cost is individual item
		self.item = item 
		self.cost = cost 
		self.quantity = quantity


class Grocery(Items):
	def __init__(self,item,cost,quantity):
		Items.__init__(self, item, cost, quantity)
		
		#groceryAdd(self,item,cost,quantity)
		##More Categories sooner *"beta categories"
	def groceryAdd(self, item, cost, quantity): 
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


	# Purpose of this function is to check whether the individual 
	# is able to purchase the item 
	#def checkGroceriePurchase(self):

#**************** Calls to construct class lists ***************#
# Should be user interface 
# Asks about the type of lists and what to add 
# Should know whether the item is in the list 

### Test Cases ###

fruit = Grocery('apple',2,3)
print(fruit.item)
print(fruit.cost)
print(fruit.quantity)
if (fruit):
	fruit.groceryAdd(fruit.item,fruit.cost,fruit.quantity)
	fruit.gList()

fruittwo = Grocery('kiwi',1,5)
print(fruittwo.item)
print(fruittwo.cost)
print(fruittwo.quantity)
if (fruittwo):
	fruittwo.groceryAdd(fruittwo.item,fruittwo.cost,fruittwo.quantity)
	fruittwo.gList()

fruitthree = Grocery('orange',3,5)
print(fruitthree.item)
print(fruitthree.cost)
print(fruitthree.quantity)
if (fruitthree):
	fruitthree.groceryAdd(fruitthree.item,fruitthree.cost,fruitthree.quantity)
	print(fruitthree.gList())




