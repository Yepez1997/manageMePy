## File Description ## 
## Author: Aureliano Yepez 
## Date: July 25, 2017
import pandas as pd
from pandas import DataFrame 
from userScript import *

listCategories = ["Restaurants", "School", "Housing","Grocery","Personal", "Custom"]
## All these empty lists are added with input data 
### Groceries ### 


## for rows ---- this is just a test
def createExcel():
	df = DataFrame({'Grocery Items': groceryItems})
	## creates excel
	df.to_excel('test.xlsx', sheet_name='sheet1', index=False)









