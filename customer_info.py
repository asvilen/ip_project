from project.customer import Customer


class CustomerTable:
    def __init__(self, customer: Customer):
        self.customer = customer

    def create_table(self):
        return {
            "Name": self.customer.name,
            "Country": self.customer.country
        }
