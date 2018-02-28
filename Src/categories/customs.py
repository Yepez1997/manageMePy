""""
custom.py keeps track of adding all custom objects into a class
@date: Feb 28 2018
@author: Aureliano Yepez
"""
customItems = []
customCost = []
customQuanity = []

"""
custom_add: stores all custom items and creates custom classes
"""
def custom_add():
    # Item, Cost, Quantity
    itemToAdd.customAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
    ## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET
    customItems.append(itemToAdd.item)
    customCost.append(itemToAdd.cost)
    customQuanity.append(itemToAdd.quantity)
    totalItems.append(itemToAdd.item)
    totalCost.append(itemToAdd.quantity)
    return 1
