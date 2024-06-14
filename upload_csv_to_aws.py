import pyodbc
import pandas as pd
from global_variables import *

# parameters for connection to sql server database
server = ''
database = 'data_base_1'
username = ''
password = ''

# create connection with AWS database
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'UID=' + username + ';'
    'PWD=' + password + ';'
)