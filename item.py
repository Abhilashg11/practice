import csv
class item:
    pay_rate = 0.8
    all = []
    def __init__(self,name:str,price:float,quantity=0):
        assert price >= 0, f"price {price} is not greater then zero"
        assert quantity >=0,f"quantity {quantity} is not greater than zero"
       
        self.__name = name
        self.price = price
        self.quantity = quantity

        item.all.append(self)
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        if len(value) > 10:
            raise Exception("yhe name is too long")
        self.__name = value
   
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
                quantity = int(i.get('quntity'))
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
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"  
    
    
