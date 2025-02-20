import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Google Sheets authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Load forecast data
forecast_data = pd.read_csv('data/forecast_results.csv')

# Open Google Sheet
sheet = client.open("Workforce Forecasting Report").sheet1

# Clear existing data
sheet.clear()

# Upload new data
sheet.update([forecast_data.columns.values.tolist()] + forecast_data.values.tolist())

print("Google Sheets updated successfully.")
