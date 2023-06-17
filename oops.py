class item:
    def calculate(self,x,y):
        return x * y


item1 = item()
item1.name = "phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate(item1.price,item1.quantity))

item2 = item()
item2.name = "laptop"
item2.price = 1000
item2.quantity = 8
print(item2.calculate(item2.price,item2.quantity))

# print("hi")

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))