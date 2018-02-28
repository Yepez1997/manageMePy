""""
custom.py keeps track of adding all custom objects into a class
"""
customItems = []
customCost = []
customQuanity = []

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
