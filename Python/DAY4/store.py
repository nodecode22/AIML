class Store:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Store.count+=1
    
    def get_info(self):
        print(f"price of {self.name} is Rs {self.price}")

    @staticmethod
    def discount(price,percent):
        new_price=price-(price*percent/100)
        print(f"NEW PRICE={new_price}")

    @classmethod
    def get_count(cls):
        print(f"The number of products in the store is {cls.count}")


s1=Store("phone",10000)
s2=Store("charger",2500)
s4=Store("cable",2000)
s3=Store("Apple Iphone 16",75000)
Store.get_count()
s1.get_info()
s2.get_info()
s3.get_info()

