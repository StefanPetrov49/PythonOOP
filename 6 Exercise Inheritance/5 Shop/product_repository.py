from Gym.product import Product
from Gym.drink import Drink
from Gym.food import Food


class ProductRepository:

    def __init__(self) -> None:
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for prod in self.products:
            if prod == product_name:
                return prod

    def remove(self, product_name: str):
        for prod in self.products:
            if prod.name == product_name:
                self.products.remove(prod)

    def __repr__(self) -> str:
        output = []
        new_line = "\n"

        for prod in self.products:
            output.append(f"{prod.name}: {prod.quantity}")
        return f'{new_line.join(output)}'


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
