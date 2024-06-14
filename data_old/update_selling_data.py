import pandas as pd
import json
import random
from datetime import datetime, timedelta

# Load the CSV files
customers = pd.read_csv('path_to/customers.csv')
products = pd.read_csv('path_to/products.csv')

# Define a function to generate a random date with seasonal trends within the last week
def generate_seasonal_date_within_week():
    # Get today's date
    today = datetime.today()
    # Calculate the date one week ago
    one_week_ago = today - timedelta(days=7)
    
    # Define the seasons with different weights for sales
    seasons = {
        'winter': (datetime(today.year, 1, 1), datetime(today.year, 3, 20), 0.8),
        'spring': (datetime(today.year, 3, 21), datetime(today.year, 6, 20), 1.2),
        'summer': (datetime(today.year, 6, 21), datetime(today.year, 9, 22), 1.0),
        'fall': (datetime(today.year, 9, 23), datetime(today.year, 12, 20), 1.1)
    }
    
    # Find the current season
    current_season = None
    for season, (start_date, end_date, _) in seasons.items():
        if start_date <= today <= end_date:
            current_season = season
            break

    start_date, end_date, _ = seasons[current_season]
    if start_date > one_week_ago:
        start_date = one_week_ago

    # Generate a random date within the last week and the current season
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    
    return start_date + timedelta(days=random_number_of_days)

# Function to add weekly transactions
def add_weekly_transactions(file_path, num_transactions=100):
    # Load the sales transactions JSON file
    with open(file_path, 'r') as file:
        sales_transactions = json.load(file)
    
    for i in range(num_transactions):
        transaction_id = f"T{len(sales_transactions) + 1}"
        customer = random.choice(customers['Customer Name'])
        product = random.choice(products['Name'])
        quantity_sold = random.randint(1, 10)
        transaction_date = generate_seasonal_date_within_week()

        new_transaction = {
            "Transaction ID": transaction_id,
            "Customer": customer,
            "Product": product,
            "Quantity Sold": quantity_sold,
            "Transaction Date": transaction_date.strftime("%Y-%m-%d")
        }
        sales_transactions.append(new_transaction)

    # Save the updated sales transactions back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(sales_transactions, file, indent=4)

# Path to the sales transactions file
file_path = 'path_to/sales_transactions.json'

# Add new transactions weekly (simulate this by calling the function)
add_weekly_transactions(file_path)

# Schedule this function to run weekly using a task scheduler or a cron job
# Example for Unix-based systems: 
# 1. Open the crontab file using `crontab -e`
# 2. Add the following line to run the script every week (adjust the path to your Python script):
# 0 0 * * 0 python3 /path_to_your_script/update_sales_transactions.py