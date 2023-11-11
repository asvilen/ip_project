import pandas as pd

from project.customer import Customer


class IPActivityTable:
    _queries = []

    def __init__(self, customer: Customer):
        self.customer = customer
        self.__query_params = self.customer.account_number
        self.df_ip_data = self.get_ip_data_as_df(self._queries, self.__query_params)

    def get_ip_data_as_df(self, queries, query_params):
        ip_data_dict = {}
        for query in queries:
            ip_data_dict[query] = self.customer.get_query_result(query, **query_params)
        return pd.concat([pd.DataFrame(ip_data_table) for ip_data_table in ip_data_dict.values()])
