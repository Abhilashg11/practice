class item:
    def __init__(self,name,price,quantity=0):
        print("hi")
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate(self):
        return self.price * self.quantity

 
item1 = item("phone",500,3)
print(item1.name)
print(item1.price)
print(item1.quantity)

print(item1.calculate())

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