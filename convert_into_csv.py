import pandas as pd
import csv
import json
import os
from global_variables import *


# create new csv files for all files with data
os.makedirs(os.path.dirname(CUSTOMERS_CSV_FILEPATH_NEW), exist_ok=True)
os.makedirs(os.path.dirname(INVENTORY_STATUS_CSV_FILEPATH_NEW), exist_ok=True)
os.makedirs(os.path.dirname(PRODUCTS_CSV_FILEPATH_NEW), exist_ok=True)
os.makedirs(os.path.dirname(SALES_TRANSACTIONS_CSV_FILEPATH_NEW), exist_ok=True)
os.makedirs(os.path.dirname(SELLERS_CSV_FILEPATH_NEW), exist_ok=True)

"""function for ceate new customers csv file with standart layout"""
def customers_csv_processed(CUSTOMERS_CSV_FILEPATH_OLD, CUSTOMERS_CSV_FILEPATH_NEW, SELLERS_CSV_FILEPATH_OLD):
    # create data frame from customers csv file
    data_frame_customers_csv = pd.read_csv(CUSTOMERS_CSV_FILEPATH_OLD)
    # change columns names in customers data frame file
    data_frame_customers_csv.columns = ['id_customer', 'name_customer', 'date_added_customer', 'region']

    # create data frame with 2 collumns from sellers csv file
    data_frame_sellers_csv = pd.read_csv(SELLERS_CSV_FILEPATH_OLD, usecols=['ID', 'Responsible for Region'])
    # change columns names in sellers data frame file
    data_frame_sellers_csv.columns = ['id_seller', 'region']

    # connection two data frames by region, adding responsible seller for the customer
    data_frame_customers_csv = pd.merge(data_frame_customers_csv, data_frame_sellers_csv, on='region', how='left')

    # change all letters for small
    data_frame_customers_csv = data_frame_customers_csv.apply(lambda x: x.lower() if type(x) == str else x)

    # save new data frame as csv file
    data_frame_customers_csv.to_csv(CUSTOMERS_CSV_FILEPATH_NEW, sep=';', index=False)


"""function for ceate new sellers csv file with standart layout"""
def sellers_csv_processed(SELLERS_CSV_FILEPATH_OLD, SELLERS_CSV_FILEPATH_NEW):
    # create data frame from sellers csv file
    data_frame_sellers_csv = pd.read_csv(SELLERS_CSV_FILEPATH_OLD)
    # change columns names in sellers data frame file
    data_frame_sellers_csv.columns = ['id_seller', 'first_name', 'last_name', 'date_employment', 'date_birth', 'region']

    # change all letters for small
    data_frame_sellers_csv = data_frame_sellers_csv.apply(lambda x: x.lower() if type(x) == str else x)

    # save new data frame as csv file
    data_frame_sellers_csv.to_csv(SELLERS_CSV_FILEPATH_NEW, sep=';', index=False)


"""function for ceate new sales_transactions csv file with standart layout"""
def sales_transactions_csv_processed(SALES_TRANSACTIONS_JSON_FILEPATH_OLD, SALES_TRANSACTIONS_CSV_FILEPATH_NEW, CUSTOMERS_CSV_FILEPATH_OLD, SELLERS_CSV_FILEPATH_OLD, PRODUCTS_CSV_FILEPATH_OLD):
    # create data frame from sales_transactions json file
    data_frame_sales_transactions_json = pd.read_json(SALES_TRANSACTIONS_JSON_FILEPATH_OLD)
    # change columns names in sales_transactions data frame file
    data_frame_sales_transactions_json.columns = ['id_transaction', 'name_customer', 'name_product', 'quantity_sold', 'date_transaction']

    # create data frame with 2 collumns from products csv file
    data_frame_products_csv = pd.read_csv(PRODUCTS_CSV_FILEPATH_OLD, usecols=['Category', 'Name', 'Unit Price'])
    # change columns names in products data frame file
    data_frame_products_csv.columns = ['category_product', 'name_product', 'unit_price']

    # connection two data frames by name_product, adding unit_price for the sale transaction
    data_frame_sales_transactions_json = pd.merge(data_frame_sales_transactions_json, data_frame_products_csv, on='name_product', how='left')
    # createnew new collumn transaction_amount
    data_frame_sales_transactions_json['transaction_amount'] = (data_frame_sales_transactions_json['unit_price'] * data_frame_sales_transactions_json['quantity_sold']).round(2)

    # create data frame with 2 collumns from customers csv file
    data_frame_customers_csv = pd.read_csv(CUSTOMERS_CSV_FILEPATH_OLD, usecols=['Customer Name', 'Region'])
    # change columns names in customers data frame file
    data_frame_customers_csv.columns = ['name_customer', 'region']

    # connection two data frames by name_customer, adding region for the sale transaction
    data_frame_sales_transactions_json = pd.merge(data_frame_sales_transactions_json, data_frame_customers_csv, on='name_customer', how='left')

    # create data frame with 2 collumns from sellers csv file
    data_frame_sellers_csv = pd.read_csv(SELLERS_CSV_FILEPATH_OLD, usecols=['ID', 'Responsible for Region'])
    # change columns names in sellers data frame file
    data_frame_sellers_csv.columns = ['id_seller', 'region']

    # connection two data frames by region, adding responsible seller for the sale transaction
    data_frame_sales_transactions_json = pd.merge(data_frame_sales_transactions_json, data_frame_sellers_csv, on='region', how='left')

    # change all letters for small
    data_frame_sales_transactions_json = data_frame_sales_transactions_json.apply(lambda x: x.lower() if type(x) == str else x)

    # save new data frame as csv file
    data_frame_sales_transactions_json.to_csv(SALES_TRANSACTIONS_CSV_FILEPATH_NEW, sep=';', index=False)


"""function for ceate new products csv file with standart layout"""
def products_csv_processed(PRODUCTS_CSV_FILEPATH_OLD, PRODUCTS_CSV_FILEPATH_NEW):
    # create data frame from products csv file
    data_frame_products_csv = pd.read_csv(PRODUCTS_CSV_FILEPATH_OLD)
    # change columns names in products data frame file
    data_frame_products_csv.columns = ['id_product', 'category_product', 'name_product', 'unit_price']

    # change all letters for small
    data_frame_products_csv = data_frame_products_csv.apply(lambda x: x.lower() if type(x) == str else x)

    # save new data frame as csv file
    data_frame_products_csv.to_csv(PRODUCTS_CSV_FILEPATH_NEW, sep=';', index=False)


"""function for ceate new inventory_status csv file with standart layout"""
def inventory_status_csv_processed(INVENTORY_STATUS_CSV_FILEPATH_OLD, INVENTORY_STATUS_CSV_FILEPATH_NEW):
    # create data frame from inventory_status csv file
    data_frame_inventory_status_csv = pd.read_csv(INVENTORY_STATUS_CSV_FILEPATH_OLD)
    # change columns names in inventory_status data frame file
    data_frame_inventory_status_csv.columns = ['id_product', 'quantity_in_stock', 'pallet_space', 'date_posting']

    # change all letters for small
    data_frame_inventory_status_csv = data_frame_inventory_status_csv.apply(lambda x: x.lower() if type(x) == str else x)

    # save new data frame as csv file
    data_frame_inventory_status_csv.to_csv(INVENTORY_STATUS_CSV_FILEPATH_NEW, sep=';', index=False)


customers_csv_processed(CUSTOMERS_CSV_FILEPATH_OLD, CUSTOMERS_CSV_FILEPATH_NEW, SELLERS_CSV_FILEPATH_OLD)
sellers_csv_processed(SELLERS_CSV_FILEPATH_OLD, SELLERS_CSV_FILEPATH_NEW)
sales_transactions_csv_processed(SALES_TRANSACTIONS_JSON_FILEPATH_OLD, SALES_TRANSACTIONS_CSV_FILEPATH_NEW, CUSTOMERS_CSV_FILEPATH_OLD, SELLERS_CSV_FILEPATH_OLD, PRODUCTS_CSV_FILEPATH_OLD)
products_csv_processed(PRODUCTS_CSV_FILEPATH_OLD, PRODUCTS_CSV_FILEPATH_NEW)
inventory_status_csv_processed(INVENTORY_STATUS_CSV_FILEPATH_OLD, INVENTORY_STATUS_CSV_FILEPATH_NEW)