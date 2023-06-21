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
    @staticmethod        
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False


    def __repr__(self):
        return f"item('{self.name}',{self.price},{self.quantity})"  
    


class phone(item):
     all = []
     def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
        assert price >= 0, f"price {price} is not greater then zero"
        assert quantity >=0,f"quantity {quantity} is not greater than zero"
        assert broken_phones >=0,f"quantity {broken_phones} is not greater than zero"
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones

        phone.all.append(self)

phone1 = phone("jcphone",500,5,1)
print(phone1.calculate())
phone2 = phone("jscphone20",700,6)



