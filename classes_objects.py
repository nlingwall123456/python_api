class Store:
    def __init__(self,name):
        self.name = name
        self.items =[]
    
    def add_item(self, name, price):
        self.price = price
        item = {"name":name, "price":price}
        self.items.append(item)
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        return sum([item["price"] for item in self.items])