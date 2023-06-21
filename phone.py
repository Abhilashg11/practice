from item import item
class phone(item):
     def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
        super().__init__(
            name,price,quantity
        )
        
        assert broken_phones >=0,f"quantity {broken_phones} is not greater than zero"
        
        self.broken_phones = broken_phones