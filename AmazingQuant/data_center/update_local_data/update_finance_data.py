# -*- coding: utf-8 -*-

# ------------------------------
# @Time    : 2019/11/21
# @Author  : gao
# @File    : download_Info_data.py
# @Project : AmazingQuant
# ------------------------------

from AmazingQuant.utils.mongo_connection_me import MongoConnect
from apps.server.database_server.database_field.field_a_share_finance_data import AShareIncome
from AmazingQuant.utils.performance_test import Timer


if __name__ == '__main__':
    database = 'stock_base_data'
    with MongoConnect(database):
        with Timer(True):
            security_code_list = AShareIncome.objects.distinct('security_code')
            data = AShareIncome.objects(security_code__in=security_code_list, statement_type=408009000)
            for i in data:
                print(i.security_code)
