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
import numpy as np
## imported classes from file items.py #######
from items import Items 
from items import Grocery
from items import Personal
from items import Custom 
from items import School 
from items import Housing 
#from items import Totals 
###############################################

################# Start #######################
print("######################################################################")
print("Welcome to ManageMe!")
print("A self budgeting appliction")
print("To start off please chose one of the categories in the list below:")
print("* Groceries")
print("* School")
print("* Housing")
print("* Personal")
print("* Custom")


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
def choseCategory():
	categoryResponse = input('What category would you like to input into your Budget list? ')
	listOfCategories = ["groceries","custom","school","housing","personal"]
	currentCategores = ["gList","cList","pList","hList","sList"]
	
	startsCategory = {"g":"groceryAdd","c":"customAdd","p":"personalAdd","h":"housingAdd","s":"schoolAdd"} #first letter of categories 
	#addfunction = {"groceryAdd":groceryAdd,"customAdd":customAdd,"personalAdd":personalAdd,"housingAdd":housingAdd,"schoolAdd":schoolAdd}
	#key= Item category name
	#value = Class Name   
	classDictionaryList = {"groceries":"Grocery","custom":"Custom","school":"School","housing":"Housing","personal":"Personal"}
	for i in listOfCategories:
		if (categoryResponse in listOfCategories): 
			# add to the classes 
			itemToAdd = input("What item would you like to add?: ")
			costToAdd = input("How much does the item cost? ")
			quantityToAdd = input("How many would you like to add?: ")
			## Make call to classes #########

			###### Take a close look at this from stack over flow ####### 
			#      exec("%s = %d" % (x,2)) 
			print(itemToAdd)
			exec("%s=%d" % (itemToAdd, 2)) # to make as a variable 
			print(itemToAdd) # we should get two if the number changes 

			for key in classDictionaryList: 
				if key in listOfCategories and categoryResponse in listOfCategories and key == categoryResponse:
					classKey = eval(classDictionaryList[key])
			itemToAdd = classKey(itemToAdd, costToAdd, quantityToAdd) ## class
			## need to know what catergories to add once in the list 
			firstLetterOfCategory = categoryResponse[0]
			for key in startsCategory: 
				if (firstLetterOfCategory == key):
					currentAdd = startsCategory[key]  #first letter of categories and VALUE
					if currentAdd == "groceryAdd":
						itemToAdd.groceryAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					if currentAdd == "customAdd":
						itemToAdd.customAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					if currentAdd == "personalAdd":	
						itemToAdd.personalAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					if currentAdd == "schoolAdd":
						itemToAdd.schoolAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					if currentAdd == "housingAdd":
						itemToAdd.housingAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)



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
			yesOrNo = input("Do you want to add another item? ")
			yesOrNo = yesOrNo.lower()
			yes = "yes"
			#yesResponses = ["yes","YES","y","YES"]
			if (yesOrNo == yes):
				choseCategory()
			else: 
				break
		else:
			print("Sorry the category " + str(categoryResponse) + " is not in the list")
			choseCategory()


choseCategory()




