class item:
    pay_rate = 0.8
    def __init__(self,name:str,price,quantity=0):
        assert price >= 0, f"price not {price}"
        assert quantity >=0,f"quantity not{quantity}"
        print("hi")
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate(self):
        return self.price * self.quantity

 
item1 = item(100,500, 1)
print(item1.name)
print(item1.price)
print(item1.quantity)

print(item.pay_rate)
print(item1.pay_rate)
# print(item1.calculate())

# item2 = item()
# item2.name = "laptop"
# item2.price = 1000
# item2.quantity = 8
# print(item2.calculate(item2.price,item2.quantity))

# print("hi")

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))