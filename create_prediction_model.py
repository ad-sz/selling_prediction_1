from global_variables import *
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import csv

# create DataFrame from data
data_selling = pd.read_csv(SALES_TRANSACTIONS_CSV_FILEPATH_NEW, delimiter=';')

# convert column with date on date format
data_selling['date_transaction'] = pd.to_datetime(data_selling['date_transaction'])

# setting column with data like an index
data_selling.set_index('date_transaction', inplace=True)

# groupping data by day (sum of transaction_amount)
daily_sales = data_selling['transaction_amount'].resample('W').sum()

# division into training and test set (last 30 days as test set)
train = daily_sales[:-5]
test = daily_sales[-5:]

# training ARIMA model (p, d, q values chosen after analysis by AI)
model = SARIMAX(train, order=(2, 0, 2))
model_fit = model.fit(disp=False)

# prediction on testing group data
predictions = model_fit.predict(start=len(train), end=len(train) + len(test) - 1, dynamic=False)

# model evaluation
mse = mean_squared_error(test, predictions)
print(f"Mean Squared Error: {mse}")

# chart
plt.figure(figsize=(10, 6))
plt.plot(train.index, train, label='Train')
plt.plot(test.index, test, label='Test')
plt.plot(predictions.index, predictions, label='Predictions', color='red')
plt.legend()
plt.show()
