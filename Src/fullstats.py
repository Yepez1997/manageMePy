## File Description ## 
## Author: Aureliano Yepez 
## Date: July 22, 2017

#should be called after everything is computed
import numpy as np
import pandas as pd 
import matplotlib as mp 
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


class Fullstats(Items): ## Should inherit items and account info or the class Totals

	def __init__(self,item,cost,quantity):
		Items.__init__(self, item, cost, quantity)

	def totalsList(self):
		print("Your current list: ")
		print("Item", "Cost")
		for key in self.listItems:
			print(key.capitalize(), self.listItems[key])
		check = "##### Manage Me #####"
		return check
		#print("-----Current List-----")
		#print("Item", "Quantity","Total Cost")
		#return self.item, self.quantity, self.quantity * self.cost

	