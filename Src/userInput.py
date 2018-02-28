"""
userInput.py hold user input information
"""

"""
user_input:  user input for neccesary information to append to classes
@ return all user input 
"""
def user_input():

    	itemToAdd = input("What item would you like to add?: ")
        costToAdd = input("How much does the item cost? ")
        quantityToAdd = input("How many would you like to add?: ")

        return itemToAdd, costToAdd, quantityToAdd
