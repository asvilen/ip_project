from project.account import Account


class Customer(Account):
    _cust_info_query = "get_customer_info"

    def __init__(self, account_number):
        super().__init__(account_number)
        self.customer_info = self.get_query_result(self._cust_info_query, self.universal_id)
        self.name = self.get_name(self.customer_info)
        self.country = self.get_country(self.customer_info)

    @staticmethod
    def get_name(df_customer_info):
        return df_customer_info["Name"]

    @staticmethod
    def get_country(df_customer_info):
        return df_customer_info["Country"]
