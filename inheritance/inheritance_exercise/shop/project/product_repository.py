from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products: List[Product] = []
        
    def add(self, product: Product) -> None:
        self.products.append(product)
        
    def find(self, product_name: str) -> None or Product:
        try:
            product = next(filter(lambda x: x.name == product_name, self.products))
        except StopIteration:
            pass
        
        return product
    
    def remove(self, product_name: str) -> None:
        if product_name in self.products:
            self.products.remove(product_name)
            
    def __repr__(self) -> str:
        return "\n".join([f"{p.name}: {p.quantity}" for p in self.products])