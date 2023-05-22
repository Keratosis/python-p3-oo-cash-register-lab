#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total= 0.0):
        self.discount = discount
        self.total = total
        self.items =[]
        self.prices = []
   
    def add_item(self,title, price, quantity =1):
        self.total +=  price * quantity
        self.items.extend([title] * quantity)
        self.prices.extend([price] * quantity)
      
      
      
    def apply_discount(self):
        if self.discount == 0:
          print("There is no discount to apply.")
          
        else:
            discount_amount = self.total * (self.discount /100)
            discounted_total= self.total - discount_amount
            self.total = discounted_total
            print(f"After the discount, the total comes to ${int(self.total)}.")
            
    def void_last_transaction(self):
       if self.items and self.prices:
        last_quantity = self.items.count(self.items[-1])
        last_price = self.prices[-1] * last_quantity
        self.total -= last_price
        del self.items[-last_quantity:]
        del self.prices[-last_quantity:]
       else:
        print("No items to void.")


# Create a CashRegister instance
cash_register = CashRegister(discount=10, total=50.0)

# Print the attributes
print(f"Discount: {cash_register.discount}")
print(f"Total: {cash_register.total}")
print(f"Items: {cash_register.items}")
print(f"Prices: {cash_register.prices}")

# Call the methods
cash_register.add_item("Apple", 1.0, 3)
cash_register.apply_discount()
cash_register.void_last_transaction()

        
    
   
      
        
      
       
              
