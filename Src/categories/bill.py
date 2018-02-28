""""
bill.py keeps track of adding all bill objects into a class
"""

#Contains bill objects that store information
billsItems = []
billsCost = []
billsQuanity = []


def bills_add():
    # Item, Cost, Quantity
    itemToAdd.billsAdd(itemToAdd.item, itemToAdd.cost,itemToAdd.quantity)
    ## APPEND TO EXCEL.PY TO SAVE DATA AND CREATE EXCEL SHEET
    billsItems.append(itemToAdd.item)
    billsCost.append(itemToAdd.cost)
    billsQuanity.append(itemToAdd.quantity)
    totalItems.append(itemToAdd.item)
    totalCost.append(itemToAdd.quantity)
    return 1 
