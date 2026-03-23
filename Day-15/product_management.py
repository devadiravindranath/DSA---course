class product:
    def __init__(self,product_id,name,price,stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def display_details(self):
        print('product_id:',self.product_id)
        print("name: ",self.name)
        print("price: ",self.price)
        print("stock",self.stock)

    def apply_discount(self,percent):
        discount_amount = self.price*percent/100
        self.price = self.price - discount_amount

    def update_stock(self,quantity):
        self.stock = self.stock + quantity

p1 = product(101,"nike shoes",2000,10)

p1.display_details()
p1.apply_discount(10)
p1.update_stock(-2)
print("\nafter update:")

p1.display_details()

