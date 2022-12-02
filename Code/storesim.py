# This is the basic template for an inventory updater. Complete the functions to add, remove, and update items in a store's inventory

#Basic function used to print out the items in a store's inventory in a more useful way than simply print(dictionary)
def printItems():
  global items #could be updated to print out both the price and the quantities of the items
  line = 1
  for item in items:
    print("\n", line, ": " + item) 
    print("    Price: $"+str(prices[item])+"\n    Quantity: "+str(quantity[item]))
    line += 1

#Sale function should take a string/item and a number as an input and update the number of items left after a day of sales
def sale(b, n):
  
  #update the quantity dictionary accordingly
  quantity[items[b-1]] -= n
  print("You have", quantity[items[b-1]],"of" , items[b-1], "left\n")


#Delivery function should take a string/item and a number as an input and update the number of items available after a delivery (an update you could make is to add items to the inventory when delivering something new to the shop - not required)
def delivery(b, n):
    
  #update the quantity dictionary accordingly
  quantity[items[b-1]] += n
  print("You have", quantity[items[b-1]], "of", items[b-1], "left\n")
  
#the priceChange function takes a string/item and a number as inputs and updates the prices accordingly
def priceChange(u, n):
  global prices
  prices[u] = n
  print(items[u-1], "is now", "$"+str(prices[items[u]]))
  #update prices and let the user know via a print statement what the new price is

#create a dictionary with 5+ items - remember to have the same keys in both dictionaries
prices = {
        "Apples": 5, 
        "Bananas": 4,
        "Grapes": 6, 
        "Blueberries": 10,
        "Chocolate": 8
        }
quantity = {
        "Apples": 10,
        "Bananas": 5, 
        "Grapes": 100,
        "Blueberries": 50,
        "Chocolate":1
        }
items = [*quantity] #this makes a list of all the keys so we can access the keys via integer indicis

printItems()

while True:
  response = input(" Press 1 for Sale \n Press 2 for Delivery \n Press 3 for Price Update \n Press 4 to Quit\n")
  if (response == '1'):
    printItems()
    #ask the user for a line number
    sale(int(input("What item was sold?\n")), int(input("How many were sold?\n")))
    #ask the user for how many items were sold
    
    #call the function to update
    #sale(items[___-1], _____)

  elif (response == '2'):
    printItems()
    #very similar to sale, but calling the delivery function
    delivery(int(input("What was delivered?\n")), int(input("How many were delivered?\n")))


  elif (response == '3'):
    printItems()
    priceChange(int(input("What item do you want to update?\n")), int(input("What is the new price?\n")))
    #get the line number for the item from the user
    
    #get the new price - should it be integers or decimals?
    #number = _____(input("New Price of "+items[_____-1]+"\n"))

    #call priceUpdate(x, y) function
    

  elif (response == '4'):
    break

#show the value of all items in the store
value = 0
for item in items:
  value += prices[item]*quantity[item] #update - definitely not 0
print("\n The value of your inventory is $"+ str(value))
