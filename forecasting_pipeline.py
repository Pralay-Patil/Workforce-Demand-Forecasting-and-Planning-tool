import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet
import joblib

# Load data
data = pd.read_csv('data/demand_data.csv', parse_dates=['date'], index_col='date')

# ARIMA Model
arima_model = ARIMA(data['demand'], order=(5,1,0))
arima_result = arima_model.fit()
joblib.dump(arima_result, 'models/arima_model.pkl')

# Prophet Model
data_prophet = data.reset_index().rename(columns={'date': 'ds', 'demand': 'y'})
prophet_model = Prophet()
prophet_model.fit(data_prophet)
joblib.dump(prophet_model, 'models/prophet_model.pkl')

print("Forecasting models saved successfully.")
