import pandas as pd
import csv
import json
import os
import subprocess
from global_variables import *
from convert_into_csv import *
from data_to_sql_table import *

# convert raw files with data
customers_csv_processed(CUSTOMERS_CSV_FILEPATH_OLD, CUSTOMERS_CSV_FILEPATH_NEW, SELLERS_CSV_FILEPATH_OLD)
sellers_csv_processed(SELLERS_CSV_FILEPATH_OLD, SELLERS_CSV_FILEPATH_NEW)
sales_transactions_csv_processed(SALES_TRANSACTIONS_JSON_FILEPATH_OLD, SALES_TRANSACTIONS_CSV_FILEPATH_NEW, CUSTOMERS_CSV_FILEPATH_OLD, SELLERS_CSV_FILEPATH_OLD, PRODUCTS_CSV_FILEPATH_OLD)
products_csv_processed(PRODUCTS_CSV_FILEPATH_OLD, PRODUCTS_CSV_FILEPATH_NEW)
inventory_status_csv_processed(INVENTORY_STATUS_CSV_FILEPATH_OLD, INVENTORY_STATUS_CSV_FILEPATH_NEW)

# # run powershell for putting data to sql table
# run_powershell_data_to_sql_table(POWERSHELL_FILEPATH)