class item:
    pay_rate = 0.8
    def __init__(self,name:str,price:float,quantity=0):
        assert price >= 0, f"price {price} is not greater then zero"
        assert quantity >=0,f"quantity {quantity} is not greater than zero"
       
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * item.pay_rate

 
item1 = item("phone",500, 1)
# item2 = item("laptop",100,3)
item1.apply_discount()
print(item1.price)
