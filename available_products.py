# AVAILABLE GROCERIES
# checks if the product selected is currently present in the inventory and the allows it to be added to cart

class AvailableGroceries:
    def __init__(self,item_name,price,addtobasket, available_groceries) :
        self.item_name=item_name
        self.addtobasket={}
        self.price=price
        self.groceries = {}
        
    def add_to_cart(self,add):
        self.add=self.addtobasket

#  ********Checking if the item selection is availabel in stock*************

        if self.item_name in self.groceries and self.price in self.groceries:
            self.add==True
            print(f"{self.item_name} added to basket")
            
        else:
            self.add == False
            print(f"{self.item_name} is not available")

#**************** returning the final state of the button "add to cart"******************

        return self.add

# ******************clling the function for a trial****************


itemOne = AvailableGroceries("kiwi", 200, False, {"kiwi": 200, "mango": 100})

print(itemOne.add_to_cart(False))