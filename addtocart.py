# Cart Management system
class Cart:
    def __init__(self, item, price):
        self.item = item
        self.prices = []
        self.cart = []
        self.total = 0
    
# Kijani groceries cart will enable our customers to add their 
# selected items to be added to the cart to make it easier to know what to pay for
    
    def add_to_cart(items):
        while true:
            item = input("Select an item (q to quit):")
            if item == "q":
                break
            else:
                price = input(f"Enter the price of {item}")
                cart.append(item)
                prices.append(price)
            for item in cart:
                print(item)
            for price in prices:
                total += price
                print(f"Your total amount is:ksh{total}")






            






    
