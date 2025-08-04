# Python Program: 
# CSC505: Principles of Software Development
# Module 3: Critical Thinking
# Professor: Dr. Bingdong Li 
# Created by Mukul Mondal
# Saturday, Aug 2nd, 2025

'''
Problem statement:

... develop.. a "first" prototype for a mobile app that let users save a shopping list on their devices.
How would you create a preliminary architectural design for it? Chose the necessary tools (UML or other 
diagramming tools) to show your strategy. Then create a series of sketches representing the key screens 
for a paper prototype for the shopping list app.

Use Python to write a script that will print out the names and number of pages in your prototype and 
the sequence or flow of the pages. Submit the source file (.py), the screenshots of a successful 
execution of your program, ...
'''

from os import system, name
from typing import List, Dict
from datetime import date, datetime

# This is just a helper function to clear the screen
# This is not required, per problem statement.
def clearScreen():    
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return


# This represents an item in the shopping store.
class StoreItem:
    def __init__(self, name:str, desc:str, price:float):
        self.Name: str = name.lstrip().rstrip()         # Item Name
        self.Description: str = desc.lstrip().rstrip()  # Item Description
        self.Price: float = price                       # Item Price

# sample data:
'''
    StoreItem('storeItem1', 'StoreItem1 Description', 2.49),
    StoreItem('storeItem2', 'StoreItem2 Description', 4.49),
    StoreItem('storeItem3', 'StoreItem3 Description', 9.49),
'''

# This represents the ShoppingStore
# ShoppingStore is just a container of all items in the store
# ShoppingStore also has a name and address
# StoreItems is a Dictionary with items name is the key, StoreItem object itself in the value.
# AddItem method can be called to add an item in the dictionary
# We can also have method like RemoveItem or ... etc.. not shown here
class ShoppingStore: 
    def __init__(self,name:str, addr:str):
        self.store_name: str = name.lstrip().rstrip()
        self.store_address: str = addr.lstrip().rstrip()
        self.StoreItems: Dict[str, StoreItem] = {}   # Dict[StoreItem name, StoreItem]
    def AddItem(self, newItem: StoreItem):
        if newItem.Name not in self.StoreItems:
            self.StoreItems[newItem.Name] = newItem        
        return

# sample data: StoreItems
'''
    'storeItem1': StoreItem('storeItem1', 'StoreItem1 Description', 2.49),
    'storeItem2': StoreItem('storeItem2', 'StoreItem2 Description', 4.49),
    'storeItem3': StoreItem('storeItem3', 'StoreItem3 Description', 9.49),
    'storeItem3': StoreItem('storeItem3', 'StoreItem3 Description', 7.49),
'''


# This represents the ShoppingCart
# ShoppingCart is just a container of all items customer selected to buy
# ShoppingCart also has the Customer name and shopping date
# ShoppingCartItems is a Dictionary with items name is the key, 'StoreItem object and Count' together is the value.
# AddItem method can be called to add an item in this dictionary
# RemoveItem method can be called to remove an item from this dictionary
# print_items_cost method can be called to know the total price of all items in the ShoppingCart.
class ShoppingCart:
    def __init__(self,cust_name:str, date:str):
        self.customer_name: str = "Customer name"
        self.shopping_date: str = "Aug 3rd, 2025"
        self.ShoppingCartItems: Dict[str, {StoreItem, int}] = {}    # Dict[StoreItem name, {StoreItem, item purchased count}]
    def AddItem(self, newItem: StoreItem):
        if newItem.Name in self.ShoppingCartItems:
            self.ShoppingCartItems[newItem.Name] += 1
        else:
            self.ShoppingCartItems[newItem.Name] = 1
        return
    
    def RemoveItem(self, newItem: StoreItem):
        if newItem.Name in self.ShoppingCartItems:
            self.ShoppingCartItems[newItem.Name] -= 1
        
        if self.ShoppingCartItems[newItem.Name] == 1:
            del self.ShoppingCartItems[newItem.Name]
        return
    
    def print_items_cost(self):
        print("All items cost = $xxx.xx")  # has to be implemented
        
# sample data: ShoppingCartItems
'''
    'storeItem1': { StoreItem('storeItem1', 'StoreItem1 Description', 2.49),  3},
    'storeItem2': { StoreItem('storeItem2', 'StoreItem2 Description', 4.49),  3}
    'storeItem3': { StoreItem('storeItem3', 'StoreItem3 Description', 9.49),  2}
    'storeItem4': { StoreItem('storeItem4', 'StoreItem4 Description', 7.49),  1}
'''



# Page: Shopping Store 
# Displays all available items in the store.
# Page 1
def ShowPage1():
    print(" ===  Page 1:   Shopping Store   === ")
    print(" ===  This is the FIRST page for 'shopping process'  === ")
    print(" ===  Displays store name: ")
    print(" ===  Displays store address: ")
    print(" ===  Please see below our today's available items in the Store === ")
    # show all items (dictionary key) in the dictionary: StoreItems in the class: ShoppingStore
    print(" ===  Customer selects items from this page and Adds in the Shopping Cart === ")
    print(" ===  When customer done selecting all the needed items, they open the Shopping Cart page === ")
    return


# Page: Shopping Cart 
# Displays all customer selected items in this page.
# Customer can update items count or remove any item from his/her selection.
# Page 2
def ShowPage2():
    print(" ===  Page 2:   Shopping Cart   === ")
    print(" ===  This is the SECOND page for 'shopping process'  === ")
    print(" ===  Displays Customer name: ")
    print(" ===  Displays Shopping date: ")
    print(" ===  Shows all customer selected items in the Shopping Cart === ")
    # show all items (dictionary key) in the dictionary: StoreItems in the class: ShoppingStore
    print(" ===  Customer can adjust item count by doing 'Substract/Remove' activity in this page === ")
    print(" ===  Then customer can select 'Checkout' button to open the next screen, Page 3 === ")
    return

# Page: Checkout and Payment
# Page 3
def ShowPage3():
    print(" ===  Page 3:   Checkout and Payment   === ")
    print(" ===  This is the THIRD page for 'shopping process'  === ")
    print(" ===  Displays Shopping store name: ")
    print(" ===  Displays store address: ")
    print(" ===  Displays Shopping date: ")
    print(" ===  Calculates total price of all items in the Shopping cart: ")
    print(" ===  Count items in the Shopping cart: ")
    print(" ===  Displays Total price of all items: $xx.xx ")
    print(" ===  Displays Total items count: xx ")
    print(" ===  Calculates applicable sales Tax  === ")
    print(" ===  Calculates Total cost by adding total price and tax  === ")
    print(" ===  Displays Total cost: $xxx.xx ")
    print(" ===  Shows buttons to Pay or Cancel === ")
    print(" ===  If Customer press Cancel then this app closes this Page 3 and goes to Page 2 === ")
    print(" ===  If Customer press Pay then system takes the payment from customer and triggers printer for receipt === ")    
    print(" ===  Then it destroys Page 2 and closes Page 3 === ")
    print(" ===  This is the end for this 'shopping process'  === ")
    return


def execute_module3_ct():
    #Create Store items
    #print(" ==== Creating StoreItem ====")
    item1 = StoreItem('storeItem1', 'StoreItem1 Description', 2.49)
    item2 = StoreItem('storeItem2', 'StoreItem2 Description', 4.49)
    item3 = StoreItem('storeItem3', 'StoreItem3 Description', 9.49)
    item4 = StoreItem('storeItem4', 'StoreItem4 Description', 7.49)

    #create shopping store object
    print(" ==== Create ShoppingStore ====")
    shoppingStoreName = input("Enter Shopping Store name: ").lstrip().rstrip()
    while len(shoppingStoreName) < 1:
         shoppingStoreName = input("Try again. Enter Shopping Store name: ").lstrip().rstrip()
    
    shoppingStoreAddress = input("Enter Shopping Store address: ").lstrip().rstrip()
    while len(shoppingStoreAddress) < 1:
         shoppingStoreAddress = input("Try again. Enter Shopping Store address: ").lstrip().rstrip()

    ShoppingStore_obj = ShoppingStore(shoppingStoreName, shoppingStoreAddress)

    #add StoreItem in shopping store object
    ShoppingStore_obj.AddItem(item1)
    ShoppingStore_obj.AddItem(item2)
    ShoppingStore_obj.AddItem(item3)
    ShoppingStore_obj.AddItem(item4)
    print(" ==== Created: ShoppingStore and added few StoreItems in the ShoppingStore ====")

    # now invoke the FIRST page (Page1), Shopping Store
    print("\n")
    ShowPage1()

    print(" ==== Create Empty Shopping Cart for a customer ====")
    customerName = input("Enter Customer name: ").lstrip().rstrip()
    while len(customerName) < 1:
         customerName = input("Try again. Enter Customer name: ").lstrip().rstrip()
    
    shoppingDate = input("Enter Shopping date: ").lstrip().rstrip()
    while len(shoppingDate) < 1:
         shoppingDate = input("Try again. Enter Shopping date: ").lstrip().rstrip()

    ShoppingCart_obj = ShoppingCart(customerName, shoppingDate)
    print(" ==== Created: Empty ShoppingCart ====")
    
    print(" === Now customer's item selection from Page1 starts ==")
    
    # now invoke the SECOND page (Page2), Shopping Cart
    print("\n")
    ShowPage2()

    ShoppingCart_obj.AddItem(item1)
    ShoppingCart_obj.AddItem(item1)
    ShoppingCart_obj.AddItem(item1)
    ShoppingCart_obj.AddItem(item2)
    ShoppingCart_obj.AddItem(item2)
    ShoppingCart_obj.AddItem(item3)
    ShoppingCart_obj.AddItem(item4)
    ShoppingCart_obj.AddItem(item4)

    # When Customer is done shopping and ready for Checkout
    # We should not check this in loop because Customer is supposed to press the button: Checkout
    Checkout_pressed = input("Are you ready to Checkout? ").lstrip().rstrip().lower()
    while len(customerName) < 1:
         Checkout_pressed = input("Try again. Enter Customer name: ").lstrip().rstrip().lower()

    # assuming user pressed Checkout button
    print("Once Customer Pressed 'Checkout' button on Page2")
    
    # now invoke the Rhird page (Page3), Checkout and Payment
    print("\n")
    ShowPage3()

    return




if __name__ == "__main__":
    clearScreen()
    print("===== Module3 Shopping Cart == MVP =====")
    execute_module3_ct()