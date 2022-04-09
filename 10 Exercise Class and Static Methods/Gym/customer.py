class Customer:
    id = 1
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.id
        Customer.id += 1
