# Aufgabe 2

class Factory:
    def __init__(self, inventory):
        self.inventory = inventory
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def manufacture_all(self):
        for product in self.products:
            product.manufacture()

    def get_inventory(self):
        return self.inventory

class Product:
    def __init__(self, name, price, is_manufactured):
        self.name = name
        self.price = price    
        self.is_manufactured = is_manufactured

    def manufacture(self):
        self.is_manufactured = True

    def get_price(self):
        return self.price
    
    def get_info(self):
        return self.name, self.price, self.is_manufactured
    
class Electronics(Product):
    def __init__(self, name, price, is_manufactured, warranty_months):
        super().__init__(name, price, is_manufactured)
        self.warranty_months = warranty_months
 
    def manufacture(self):
        # manufacture code
        pass

class Furniture(Product):
    def __init__(self, name, price, is_manufactured, material):
        super().__init__(name, price, is_manufactured)
        self.material = material
    
    def manufacture(self):
        # manufacture code
        pass
