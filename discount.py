import csv
class item:
    pay_rate = 0.8
    all = []
    def __init__(self,name:str,price:float,quantity=0):
        assert price >= 0, f"price {price} is not greater then zero"
        assert quantity >=0,f"quantity {quantity} is not greater than zero"
       
        self.name = name
        self.price = price
        self.quantity = quantity

        item.all.append(self)
    def calculate(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * item.pay_rate
    @classmethod
    def instantiate_from_csv(cls): 
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items1 =  list(reader)
        for i in  items1:
            item(
                name = i.get("name"),
                price = float(i.get('price')),
                quantity = int(i.get('quantity'))
            )
            

    def __repr__(self):
        return f"item('{self.name}',{self.price},{self.quantity})"  
    


item.instantiate_from_csv()
print(item.all)