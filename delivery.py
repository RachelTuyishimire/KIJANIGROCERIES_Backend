import uuid
# Inganji wants to track the delivery by its Id(show the products, ), assign delivery

#  Inganji would like to have Location APIS. To know whose driver and mama mboga are in the nearest places
# as to know, which diver to send and to which mama_mboga
class Delivery:

    def __init__(self, recepient__name,deliveryId,driver_name,recepient__phone,delivery_adress,delivery_date,delivery_status):
        self.recepient__phone= recepient__phone
        self.deliveryId= deliveryId
        self.recepient__name= recepient__name
        self.delivery_adress= delivery_adress
        self.driver_name= driver_name
        self.delivery_date= delivery_date
        self.delivery_status=  delivery_status
    # def generate_deliveryId():
    def generate_deliveryId(self):
        deliveryId = str(uuid.uuid4())[:6].upper()
        return deliveryId
     
    def get_delivery_details(self):
        return (f"delivery: {self.deliveryId} recepient: {self.recepient__name} phone:  {self.recepient__phone} adress: {self.delivery_adress} date:{self.delivery_status}")

    def assign_driver(self):
        return (f"{self.driver_name} is assigned{self.deliveryId}")   

    
    def cancel_delivery(self):

        self.delivery_status = "Cancelled"   

        return (f"the delivery {self.deliveryId} is {self.delivery_status}") 