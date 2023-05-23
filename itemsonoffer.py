# itemson_offer is a class that shows the item on offer,its offer price and the option to add to cart.
# It also enables the user to check if the item is actually on offer
# if true the user successfully add it to cart
 
class Itemson_offer:
    def __init__(self, item_name, price, items_on_offer, add_to_cart):
        self.item_name = item_name
        self.price = price
    
        self.items_on_offer ={}
        self.add_to_cart={}
    def check_offers(self):
        if self.item_name in self.items_on_offer.keys():
            self.add_to_cart.self.item_name = self.price
        return self.add_to_cart

offer_item = Itemson_offer("Banana", 200, {"mango":200, "Banana":200 }, True)

print(offer_item.check_offers())