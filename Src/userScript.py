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

################# Start #######################
print("######################################################################")
print("Welcome to ManageMe!")
print("A self budgeting appliction")
print("To start off please chose one of the categories in the list below:")
print("* Groceries")
print("* School")
print("* House")
print("* Personal")
print("* Custom")


## Can implement the Ratcliff and Obershelp Algorithm for word correcting purposess
## If two words are compared and there is a 60 perecent or greater between the words then 
## we can ask "did you mean ?" else we can ask again 
## Compare raw_input versus the actual word in the listOfCatergories 

# list of catergories, still more to be added

#P1 --- list of words dataBase  
#My imlplemenation of the Ratcliff algorthm concept
listOfCategories = ["groceries","custom","school","housing","personal"]
categoryResponse = input("What would you like to input into your Budget list? ")
if (categoryResponse):
	charactersOfInput = list(categoryResponse) # characters of input 
	for category in listOfCategories: 
		categoryListWordChar = list(category) ## Gives me a matrix of the words 
		print(categoryListWordChar)


else: 
	categoryResponse





