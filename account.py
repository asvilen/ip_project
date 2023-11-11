class Account:
    _uni_query_name = "get_uni_id"

    def __init__(self, account_number: str):
        self.account_number = account_number
        self.universal_id = self.get_query_result(self._uni_query_name, {"account_number": self.account_number})

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, value: str):
        if (value is None
                or not value.isnumeric()
                or value == ""):
            return "Please enter an account number"

        self.__account_number = value

    @property
    def universal_id(self):
        return self.__universal_id

    @universal_id.setter
    def universal_id(self, value):
        if value == 0:
            return "Please enter a valid account number"

        self.__universal_id = value

    @staticmethod
    def get_query_result(self, query_name, **query_params):
        result = True
        return result
