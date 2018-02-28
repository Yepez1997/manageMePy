## File Description ##
## Author: Aureliano Yepez
## Date: July 30u, 2017

import sys
import numpy as np
import pandas as pd
from pandas import DataFrame
from excel import *


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
from items import Restaurants

## import all files from categories ##
from ./categories import * #double check

##create hash function for accesing and setting up info ? sounds like a agood idea s

## also need to iterate through all total items
## make sure the input the is put in is the right time
## Specialize each category to be user friendly
## Can implement the Ratcliff and Obershelp Algorithm for word correcting purposess ?

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
print("* Restaurants   * Hygiene")t
print("######################################################################")


## Total Objects
totalItems = []
totalCost = []
totalQuaninty = []

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
	global hygieneCost
	global hygieneQuanity
	global totalItems
	global totalCost


	## User Input
	category_ response = input('What category would you like to input into your Budget list? ')

	list_of_categories = ["groceries","custom","school","housing","personal","restaurants","bills","travel","clothing","hygiene","transportation","utilities"]
	class_dictionary_list = {"groceries":"Grocery","custom":"Custom","school":"School","housing":"Housing","personal":"Personal", "restaurants":"Restaurants",
		"bills":"Bills", "utilities":"Utilities","travel":"Travel","transportation":"Transportation","clothing":"Clothing","hyiene":"Hygiene"}

	for i in list_of_categories:
		## First check if we are in the categories
		if (categoryResponse in listOfCategories):

			itemToAdd, costToAdd, quantityToAdd = user_input()
			## user_input

			## We want to call a function to call all user input and return all user input


			## Make call to classes #########

			###### Take a close look at this from stack over flow #######
			exec("%s=%d" % (itemToAdd, 2)) # to make as a variable

			########### IMPORTANT INFORMATION ########### THIS IS WHERE THE ERROR OCCURS

			for key in class_dictionary_list:
				if key in class_dictionary_list and key == categoryResponse:
					classKey = eval(classDictionaryList[key])
					itemToAdd = classKey(itemToAdd, costToAdd, quantityToAdd) ## class
			## need to know what catergories to add once in the list


			## THIS NEEDS TO BE FIXED
			## neccesary to have to iterate throught every letter
			## what if we take the first 5 letters and compare to strings that would be used
			firstLetterOfCategory = categoryResponse[0] ## THIS NEEDS TO BE FIXED

			fiveStringLetterCategories  = ["groce", "schoo","perso","housi","custo","resta","bills","resta","perso","bills","utili","trave","trans","cloth","hygie" ]
			#for key in startsCategory:
			### set the user input to different values fot it to be processec
			## think of better way to search and access information

			for currentString in fiveStringLetterCategories:

				# Grocery add
				if  (currentString == "groce"):
					## Item, Cost, Quantity
					itemToAdd.groceryAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET
					groceryItems.append(itemToAdd.item)
					groceryCost.append(itemToAdd.cost)
					groceryQuanity.append(itemToAdd.quantity)
					totalItems.append(itemToAdd.item)
					totalCost.append(itemToAdd.quantity)
					##grocery_add
					break


				# Custom Add
				if  (currentString == "custo"):
					custom_add()
					break


				#Personal Add
				if  (currentString == "perso"):
					# Item, Cost, Quantity
					itemToAdd.personalAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET
					personalItems.append(itemToAdd.item)
					personalCost.append(itemToAdd.cost)
					personalQuanity.append(itemToAdd.quantity)
					totalItems.append(itemToAdd.item)
					totalCost.append(itemToAdd.quantity)
					personal_add()
					break


				#School Add
				if (currentString == "schoo"):
					# Item, Cost, Quantity
					itemToAdd.schoolAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET
					schoolItems.append(itemToAdd.item)
					schoolCost.append(itemToAdd.cost)
					schoolQuanity.append(itemToAdd.quantity)
					totalItems.append(itemToAdd.item)
					totalCost.append(itemToAdd.quantity)
					school_add()
					break


				#Housing Add
				if  (currentString == "housi"):
					# Item, Cost, Quantity
					itemToAdd.housingAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET
					housingItems.append(itemToAdd.item)
					housingCost.append(itemToAdd.cost)
					housingQuanity.append(itemToAdd.quantity)
					totalItems.append(itemToAdd.item)
					totalCost.append(itemToAdd.quantity)
					housing_add()
					break


				#Restuarants Add
				if  (currentString == "resta"):
					# Item, Cost, Quantity
					itemToAdd.housingAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET
					restaurantsItems.append(itemToAdd.item)
					restaurantsCost.append(itemToAdd.cost)
					restaurantsQuanity.append(itemToAdd.quantity)
					totalItems.append(itemToAdd.item)
					totalCost.append(itemToAdd.quantity)
					restuarants_add()
					break


				#Bills Add
				if  (currentString == "bills"):
					## call function that adds all builds
					bills_add()
					break

				#Utilities Add
				if  (currentString == "utili"):
					# Item, Cost, Quantity
					itemToAdd.utilitiesAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET
					utilitiesItems.append(itemToAdd.item)
					utilitiesCost.append(itemToAdd.cost)
					utilitiesQuanity.append(itemToAdd.quantity)
					totalItems.append(itemToAdd.item)
					totalCost.append(itemToAdd.quantity)
					utilities_add()
					break


				#Travel Add
				if (currentString == "trave"):
					# Item, Cost, Quantity
					itemToAdd.travelAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET
					travelItems.append(itemToAdd.item)
					travelCost.append(itemToAdd.cost)
					travelQuanity.append(itemToAdd.quantity)
					totalItems.append(itemToAdd.item)
					totalCost.append(itemToAdd.quantity)
					travel_add()
					break


				#Transportation add
				if  (currentString == "trans"):
					# Item, Cost, Quantity
					itemToAdd.transportationAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET
					transportationItems.append(itemToAdd.item)
					transportationCost.append(itemToAdd.cost)
					transportationQuanity.append(itemToAdd.quantity)
					totalItems.append(itemToAdd.item)
					totalCost.append(itemToAdd.quantity)
					transportaion_add()
					break


				#Clothing Add
				if  (currentString == "cloth"):
					# Item, Cost, Quantity
					itemToAdd.clothingAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET
					clothingItems.append(itemToAdd.item)
					clothingCost.append(itemToAdd.cost)
					clothingQuanity.append(itemToAdd.quantity)
					totalItems.append(itemToAdd.item)
					totalCost.append(itemToAdd.quantity)
					clothing_add()
					break


				#Hygiene Add
				if (currentString == "hygie"):
					# Item, Cost, Quantity
					itemToAdd.hygieneAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
					## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET
					hygieneItems.append(itemToAdd.item)
					hygieneCost.append(itemToAdd.cost)
					hygieneQuanity.append(itemToAdd.quantity)
					totalItems.append(itemToAdd.item)
					totalCost.append(itemToAdd.quantity)
					hygiene_add()
					break

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

				##stats = Fullstats("Complete List",1,1) #defaulted to 1
				#print(stats.totalsList())
				#listCat = DataFrame
				## creates excel
				## need to create series to allow to put into excel
				## also to prevent Value errror - array sizing
				############ Uses Pandas and DataFrame ############
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

				transportation1 = pd.Series(transportationItems, name='Transportation Items')
				transportation2 = pd.Series(transportationCost, name='Transportation Cost')
				transportation3 = pd.Series(transportationQuanity, name='Transportation Quanity')

				util1 = pd.Series(utilitiesItems, name='Utilities Items')
				util2 = pd.Series(utilitiesCost, name='Utilities Cost')
				util3 = pd.Series(utilitiesQuanity, name='Utilities Quanity')

				clothing1 = pd.Series(clothingItems, name='Clothing Items')
				clothing2 = pd.Series(clothingCost, name='Clothing Cost')
				clothing3 = pd.Series(clothingQuanity, name='Clothing Quanity')

				hyg1 = pd.Series(hygieneItems, name='Hygiene Items')
				hyg2 = pd.Series(hygieneCost, name='Hygiene Cost')
				hyg3 = pd.Series(hygieneQuanity, name='Hygiene Quanity')

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

				df.to_excel('managemethree.xlsx', sheet_name='Data', index=False)

				############ Uses Pandas and DataFrame ############

				sys.exit() ## terminates

		else:
			print("Sorry the category " + str(categoryResponse) + " is not in the list")
			choseCategory()


## start program
choseCategory()
