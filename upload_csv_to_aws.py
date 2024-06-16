import pyodbc
import pandas as pd
from global_variables import *

# parameters for connection to SQL server database
server = ''
database = ''
username = ''
password = ''

# create connection with AWS database
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'UID=' + username + ';'
    'PWD=' + password + ';'
    'TrustServerCertificate=yes;'
)

# function to upload CSV data to AWS server
def upload_csv_to_rds(file_path, table_name, conn):
    # read the CSV file into a DataFrame
    df = pd.read_csv(file_path, delimiter=';')
    
    # fill NaN values with None to handle SQL nulls correctly
    df = df.where(pd.notnull(df), None)

    # create cursor to execute sql command
    cursor = conn.cursor()

    # iterate through reach row in DataFrame
    for index, row in df.iterrows():
        # create list of collumns as a string
        columns = ', '.join(row.index)
        # create list of replacement values (?) for sql querry
        placeholders = ', '.join(['?' for _ in row])
        # create sql querry to insert data
        sql_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        # transforming row value to replace NaN with None
        values = [None if pd.isna(value) else value for value in row]
        print(f"SQL Query: {sql_query}")
        print(f"Values: {values}")

        try:
            # ececuting sql querry with the appropriate values
            cursor.execute(sql_query, values)
        except Exception as e:
            print(f"Error inserting row {index} into {table_name}: {e}")

    # transaction approval
    conn.commit()
    # closing the cursor
    cursor.close()

# dictionary that maps CSV file paths to table names in the database
file_table_mapping = {
    PRODUCTS_CSV_FILEPATH_NEW: 'products',
    SALES_TRANSACTIONS_CSV_FILEPATH_NEW: 'sales_transactions',
    SELLERS_CSV_FILEPATH_NEW: 'sellers',
    CUSTOMERS_CSV_FILEPATH_NEW: 'customers',
    INVENTORY_STATUS_CSV_FILEPATH_NEW: 'inventory_status'
}

# iterate through each filepath-tablename pair
for file_path, table_name in file_table_mapping.items():
    print(f"Uploading data from {file_path} to {table_name}")
    # calling a function to load data from a CSV file into the appropriate table
    upload_csv_to_rds(file_path, table_name, conn)

# closing the connection to the database when the data load is complete
conn.close()