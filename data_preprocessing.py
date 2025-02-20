import pandas as pd

# Load raw data
data = pd.read_csv('data/raw_demand_data.csv')

# Convert date column to datetime format
data['date'] = pd.to_datetime(data['date'])

# Handle missing values
data.fillna(method='ffill', inplace=True)

# Aggregate data if necessary
data = data.groupby('date').sum().reset_index()

# Save cleaned data
data.to_csv('data/demand_data.csv', index=False)

print("Data preprocessing complete. Cleaned data saved.")
