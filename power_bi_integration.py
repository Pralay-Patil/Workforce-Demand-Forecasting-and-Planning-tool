import pandas as pd

# Load forecast data
forecast_data = pd.read_csv('data/forecast_results.csv')

# Export to Power BI-compatible format
forecast_data.to_csv('data/forecast_results_powerbi.csv', index=False)

print("Data prepared for Power BI integration.")
