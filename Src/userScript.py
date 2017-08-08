## File Description ## 
## Author: Aureliano Yepez 
## Date: July 30u, 2017
'''
# This is hard coded 
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

## try to find a way to make this user friendly
## *********** NEEDS TO BE TESTED 
totals = Total() ##Should just calls itself 
print(totals.groceriesIter())
print(totals.housingIter())
print(totals.personalIter())
print(totals.schoolIter())
print(totals.customIter())
print(totals.Totals())
'''
import sys
import numpy as np
import pandas as pd
from pandas import DataFrame 
from excel import * 


#from pyspark.sql.types import StructType
## imported classes from file items.py #######
from types import *
from items import Items 
from items import Grocery
from items import Personal
from items import Custom 
from items import School 
from items import Housing 
from items import Bills 
from items import Utilities 
from items import Travel
from items import Transportation
from items import Clothing 
from items import Hygiene 


from fullstats import Fullstats
#from items import Totals 
###############################################

################# Start #######################
print("######################################################################")
print("Welcome to ManageMe!")
print("A self budgeting appliction")
print("To start off please chose one of the categories in the list below:")
print("* Groceries     * Bills")
print("* School        * Utilities")
print("* Housing       * Travel")
print("* Personal      * Transportation")
print("* Custom        * Clothing")
print("* Restaurants   * Hygiene")


## Can implement the Ratcliff and Obershelp Algorithm for word correcting purposess
## If two words are compared and there is a 60 perecent or greater between the words then 
## we can ask "did you mean ?" else we can ask again 
## Compare raw_input versus the actual word in the listOfCatergories 

# list of catergories, still more to be added

#P1 --- list of words dataBase  
#My imlplemenation of the Ratcliff algorthm concept
"""
listOfCategories = ["groceries","custom","school","housing","personal"]
listOfCatergoriesIndex = [0,1,2,3,4] #still neds updates 
categoryResponse = input("What would you like to input into your Budget list? ")
if (categoryResponse):
	charactersOfInput = list(categoryResponse) # characters of input 
	print(charactersOfInput)
	print("########################################")
	for category in listOfCategories: 
		categoryListWordChar = list(category) ## Gives me a matrix of the words 
		print(categoryListWordChar)
		StackOfCorrect = [] #Where we want to append and take off words in the list 
		# wordsInCommon = 
		for charInput in categoryResponse: 
			#for cate
			if charInput in category:
				#print(charInput)

				# if charInput in one of the matrix, we should append it to the StackOfCorrect
				# we want to compare one matrix row at a time 
				# each matrix row is a word, so in esence compare each word's chars with input chars 
				# **** from there find a way to get the perctage of words anc compare

				StackOfCorrect.append(charInput)
				print(StackOfCorrect)
				
else: 
	categoryResponse


## Recursion as an alternate path -- probably more effective
listOfCategories = ["groceries","custom","school","housing","personal"]
listOfCatergoriesIndex = [0,1,2,3,4] #still neds updates 


categoryResponse = list(categoryResponse)

if 

class TwoStrings

	def __init__(stringOne,stringTwo):
		self.stringOne = stringOne
		self.stringTwo = stringTwo


"""


## globals are in excel.py
groceryItems = []
groceryCost = []
groceryQuanity = [] 
### Restaurants ### 
restaurantsItems = []
restaurantsCost = []
restaurantsQuanity = [] 
### School ###
schoolItems = [] 
schoolCost = []
schoolQuanity = []
### Housing ###
housingItems =[]
housingCost = [] 
housingQuanity =[]
### Personal ### 
personalItems = [] 
personalCost = []
personalQuanity = [] 
### Custom ### 
customItems = [] 
customCost = [] 
customQuanity = []
### Bills ###
billsItems = [] 
billsCost = [] 
billsQuanity = []
### Utilities ###
utilitiesItems = [] 
utilitiesCost = [] 
utilitiesQuanity = []
### Travel ###
travelItems = [] 
travelCost = [] 
travelQuanity = []
### Transportation ###
transportationItems = [] 
transportationCost = [] 
transportationQuanity = []
### Clothing ###
clothingItems = [] 
clothingCost = [] 
clothingQuanity = []
### Hygiene ###
hygieneItems = [] 
hygienCost = [] 
hygieneQuanity = []



def choseCategory():

	global groceryItems
	global groceryCost
	global groceryQuanity
	global restaurantsItems
	global restaurantsCost
	global restaurantsQuanity
	global schoolItems
	global schoolCost
	global schoolQuanity
	global housingItems
	global housingCost 
	global housingQuanity
	global personalItems
	global personalCost
	global personalQuanity
	global customItems 
	global customCost 
	global customQuanity
	global billsItems
	global billsCost
	global billsQuanity
	global utilitiesItems
	global utilitiesCost
	global utilitiesQuanity
	global travelItems
	global travelCost
	global travelQuanity
	global transportationItems
	global transportationCost
	global transportationQuanity
	global clothingItems
	global clothingCost
	global clothingQuanity
	global hygieneItems
	global hygienCost
	global hygieneQuanity

	categoryResponse = input('What category would you like to input into your Budget list? ')
	listOfCategories = ["groceries","custom","school","housing","personal","restaurants","bills","travel","clothing","hygiene","transportation","utilities"]
	currentCategores = ["gList","cList","pList","hList","sList","rList","xList","yList","zList","tList","uList","bList"]
	
	## MAKE SPECIFIC CASES ## 
	startsCategory = {"g":"groceryAdd","c":"customAdd","p":"personalAdd","h":"housingAdd","s":"schoolAdd", "r":"restaurantsAdd", "b":"billsAdd",
						"u":"utilitiesAdd","t":"travelAdd","t":"transportationAdd","c":"clothingAdd","h":"hygieneAdd"} #first letter of categories 
	#addfunction = {"groceryAdd":groceryAdd,"customAdd":customAdd,"personalAdd":personalAdd,"housingAdd":housingAdd,"schoolAdd":schoolAdd}
	#key= Item category name
	#value = Class Name   
	classDictionaryList = {"groceries":"Grocery","custom":"Custom","school":"School","housing":"Housing","personal":"Personal", "restaurants":"Restaurants",
		"bills":"Bills", "utilities":"Utilities","travel":"Travel","transportation":"Transportation","clothing":"Clothing","hyiene":"Hygiene"}
	for i in listOfCategories:
		if (categoryResponse in listOfCategories): 
			# add to the classes 
			itemToAdd = input("What item would you like to add?: ")
			#assert type(itemToAdd) is StringType, "Item is not a string: %r" % itemToAdd
			costToAdd = input("How much does the item cost? ")
			#assert type(costToAdd) is IntType, "cost is not an integer: %r" % costToAdd
			quantityToAdd = input("How many would you like to add?: ")
			#assert type(quantityToAdd) is IntType, "cost is not an integer: %r" % quantityToAdd
			## Make call to classes #########

			###### Take a close look at this from stack over flow ####### 
			#      exec("%s = %d" % (x,2)) 
			#print(itemToAdd) USE TO DEBUG 
			exec("%s=%d" % (itemToAdd, 2)) # to make as a variable 
			#print(itemToAdd) # we should get two if the number changes 

			for key in classDictionaryList: 
				if key in listOfCategories and categoryResponse in listOfCategories and key == categoryResponse:
					classKey = eval(classDictionaryList[key])
			itemToAdd = classKey(itemToAdd, costToAdd, quantityToAdd) ## class
			## need to know what catergories to add once in the list 
			# *******************************************************
			## THIS NEEDS TO BE FIXED 
			firstLetterOfCategory = categoryResponse[0] ## THIS NEEDS TO BE FIXED 
			## THIS NEEDS TO BE FIXED 
			for key in startsCategory: 
				if (firstLetterOfCategory == key):
					currentAdd = startsCategory[key]  #first letter of categories and VALUE
					if currentAdd == "groceryAdd":
						## Item, Cost, Quantity 
						itemToAdd.groceryAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
						## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET 
						groceryItems.append(itemToAdd.item)
						groceryCost.append(itemToAdd.cost)
						groceryQuanity.append(itemToAdd.quantity)


					if currentAdd == "customAdd":
						# Item, Cost, Quantity 
						itemToAdd.customAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
						## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET 
						customItems.append(itemToAdd.item)
						customCost.append(itemToAdd.cost)
						customQuanity.append(itemToAdd.quantity)

					if currentAdd == "personalAdd":	
						# Item, Cost, Quantity 
						itemToAdd.personalAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
						## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET 
						personalItems.append(itemToAdd.item)
						personalCost.append(itemToAdd.cost)
						personalQuanity.append(itemToAdd.quantity)

					if currentAdd == "schoolAdd":
						# Item, Cost, Quantity 
						itemToAdd.schoolAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
						## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET 
						schoolItems.append(itemToAdd.item)
						schoolCost.append(itemToAdd.cost)
						schoolQuanity.append(itemToAdd.quantity)
					if currentAdd == "housingAdd":
						# Item, Cost, Quantity 
						itemToAdd.housingAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
						## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET 
						housingItems.append(itemToAdd.item)
						housingCost.append(itemToAdd.cost)
						housingQuanity.append(itemToAdd.quantity)
					if currentAdd == "restaurantsAdd":
						# Item, Cost, Quantity 
						itemToAdd.housingAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
						## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET 
						restaurantsItems.append(itemToAdd.item)
						restaurantsCost.append(itemToAdd.cost)
						restaurantsQuanity.append(itemToAdd.quantity)

					if currentAdd == "billsAdd":
						# Item, Cost, Quantity 
						itemToAdd.billsAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
						## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET 
						billsItems.append(itemToAdd.item)
						billsCost.append(itemToAdd.cost)
						billsQuanity.append(itemToAdd.quantity)

					if currentAdd == "utilitiesAdd":
						# Item, Cost, Quantity 
						itemToAdd.utilitiesAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
						## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET 
						utilitiesItems.append(itemToAdd.item)
						utilitiesCost.append(itemToAdd.cost)
						utilitiesQuanity.append(itemToAdd.quantity)

					if currentAdd == "travelAdd":
						# Item, Cost, Quantity 
						itemToAdd.travelAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
						## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET 
						travelItems.append(itemToAdd.item)
						travelCost.append(itemToAdd.cost)
						travelQuanity.append(itemToAdd.quantity)

					if currentAdd == "transportationAdd":
						# Item, Cost, Quantity 
						itemToAdd.transportationAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
						## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET 
						transportationItems.append(itemToAdd.item)
						transportationCost.append(itemToAdd.cost)
						transportationQuanity.append(itemToAdd.quantity)

					if currentAdd == "clothingAdd":
						# Item, Cost, Quantity 
						itemToAdd.clothingAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
						## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET 
						clothingItems.append(itemToAdd.item)
						clothingCost.append(itemToAdd.cost)
						clothingQuanity.append(itemToAdd.quantity)

					if currentAdd == "hygieneAdd":
						# Item, Cost, Quantity 
						itemToAdd.hygieneAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
						## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET 
						hygieneItems.append(itemToAdd.item)
						hygieneCost.append(itemToAdd.cost)
						hygieneQuanity.append(itemToAdd.quantity)


					#for key in addfunction:
					#	if key == currentAdd:
					#		print(key)
							
							#itemToAdd.addfunction[key]() # should print a function
							#exec("%s=%d" % (currentAdd, 2)) # to make as a variable 
							#print(itemToAdd.currentAdd())



			#firstLetterOfCategorie = itemToAdd.item[0]

			
			###################################
			## Works !!!!!!!!! CREATES CLASSES 
			print("Succesfully added a category for: " + str(categoryResponse))
			print("You have added " + str(itemToAdd.quantity)+ " " + str(itemToAdd.item) +"(s)" + " at a price of " + costToAdd + " each" )
			yesOrNo = input("Do you want to add another item? (yes/no) ")
			yesOrNo = yesOrNo.lower()
			yes = "yes"
			yes = yes.lower()
			no = "no"
			no = no.lower()
			#yesResponses = ["yes","YES","y","YES"]
			if (yesOrNo == yes):
				choseCategory()
			if (yesOrNo == no):
				print("Okay, here is a complete list of your items: ")
				stats = Fullstats("Complete List",1,1) #defaulted to 1 
				print(stats.totalsList())
				#listCat = DataFrame
				## creates excel
				## need to create series to allow to put into excel 
				## also to prevent Value errror - array sizing 
				#############
				##   key   ##
				##1 = items##
				##2 = cost ##
				##3 = quant##
				#############
				groceries1 = pd.Series(groceryItems, name='Grocery Items')
				groceries2 = pd.Series(groceryCost, name='Grocery Cost')
				groceries3 = pd.Series(groceryQuanity, name='Grocery Quanity')

				housing1 = pd.Series(housingItems,name='Housing Items')
				housing2 = pd.Series(housingCost, name='Housing Cost')
				housing3 = pd.Series(housingQuanity,name ='Housing Quanity')

				personal1 = pd.Series(personalItems,name='Personal Items')
				personal2 = pd.Series(personalCost, name='Personal Cost')
				personal3 = pd.Series(personalQuanity, name= 'Personal Quanity')

				custom1 = pd.Series(customItems, name='Custom Items')
				custom2 = pd.Series(customCost, name='Custom Cost')
				custom3 = pd.Series(customQuanity, name='Custom Quanity')

				school1 = pd.Series(schoolItems, name='School Items')
				school2 = pd.Series(schoolCost, name='School Cost')
				school3 = pd.Series(schoolQuanity, name='School Quanity')

				restau1 = pd.Series(restaurantsItems, name='Restaurants Items')
				restau2 = pd.Series(restaurantsCost, name='Restaurants Cost')
				restau3 = pd.Series(restaurantsQuanity, name='Restaurants Quanity')

				travel1 = pd.Series(travelItems, name='Travel Items')
				travel2 = pd.Series(travelCost, name='Travel Cost')
				travel3 = pd.Series(travelQuanity, name='Travel Quanity')

				bills1 = pd.Series(billsItems, name='Bill Items')
				bills2 = pd.Series(billsCost, name='Bill Cost')
				bills3 = pd.Series(billsQuanity, name='Bill Quanity')

				transportation1 = pd.Series(transportionItems, name='Transportation Items')
				transportation2 = pd.Series(transportationCost, name='Transportation Cost')
				transportation3 = pd.Series(transportationQuanity, name='Transportation Quanity')

				util1 = pd.Series(utilitiesItems, name='Utilities Items')
				util2 = pd.Series(utilitiesCost, name='Utilities Cost')
				util3 = pd.Series(utilitiesQuanity, name='Utilities Quanity')

				clothing1 = pd.Series(clothingItems, name='Clothing Items')
				clothing2 = pd.Series(clothingCost, name='Clothing Cost')
				clothing3 = pd.Series(clothingQuanity, name='Clothing Quanity')

				hyg1 = pd.Series(hygieneItems, name='Hygiene Items')
				hyg2 = pd.Series(hyieneCost, name='Hygiene Cost')
				hyg3 = pd.Series(hygieneQuanity, name='Hygiene Quanity')

				#df = pd.DataFrame(({'Grocery Items': groceryItems, 'Grocery Cost': groceryCost,'Grocery Quanity':groceryQuanity,
				#	'Housing Items': housingItems,'Housing Cost': housingCost, 'Housing Quanity':housingQuanity,
				#	'School Items': schoolItems, 'School Cost': schoolCost, 'School Quanity': schoolQuanity,
				#	'Restaurants Items': restaurantsItems, 'Restaurants Cost': restaurantsCost, 'Restaurants Quanity': restaurantsQuanity,
				#	'Personal Items': personalItems, 'Personal Cost': personalCost, 'Personal Quanity': personalQuanity,
				#	'Custom Items': customItems, 'Custom Cost': customCost, 'Custom Quanity': customQuanity, }))
				#df.transpose()
				## Works ##
				df = pd.concat([groceries1,groceries2,groceries3
								,housing1, housing2, housing3
								,personal1, personal2, personal3
								,custom1, custom2, custom3 
								,school1, school2, school3
								,restau1,restau2,restau3
								,bills1, bills2, bills3
								,transportation1, transportation2, transportation3
								,util1, util2, util3
								,clothing1, clothing2, clothing3
								,hyg1, hyg2, hyg3
								,travel1, travel2, travel3 ], axis=1)

				df.to_excel('managemeTest.xlsx', sheet_name='sheet1', index=False)
				sys.exit() ## terminates 
				## break only went to the next line
		else:
			print("Sorry the category " + str(categoryResponse) + " is not in the list")
			choseCategory()


choseCategory()




