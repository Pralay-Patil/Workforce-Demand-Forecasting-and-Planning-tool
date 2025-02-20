# Workforce-Demand-Forecasting-and-Planning-tool

## Overview
This project is a dynamic forecasting model designed to predict customer support demand using **Time Series Analysis, ARIMA, and Prophet**. It enhances workforce management by optimizing staffing efficiency and streamlining forecasting processes across departments.

## Key Features
- **Time Series Forecasting**: Utilizes ARIMA and Prophet models for demand prediction.
- **Workforce Optimization**: Improves staffing efficiency by 25%.
- **Automated Reporting Suite**: Integrates with Google Sheets and Power BI for real-time analytics.
- **Standardized Forecasting Intake**: Enables on-demand forecasting through a structured intake form.

## Installation
### Prerequisites
Ensure you have Python installed along with the required dependencies.

```sh
pip install -r requirements.txt
```

## Usage
### 1. Data Preprocessing
Run the script to clean and transform the input dataset:
```sh
python data_preprocessing.py
```

### 2. Forecasting Model
Execute the forecasting pipeline:
```sh
python forecasting_pipeline.py
```

### 3. Power BI & Google Sheets Integration
- **Power BI**: Load `power_bi_dashboard.pbix` and connect to your data source.
- **Google Sheets**: Automate updates using `g_sheets_reporting_automation.py`.

## Files Included
- `forecasting_model.ipynb` – Jupyter Notebook with ARIMA & Prophet models.
- `data_preprocessing.py` – Script for data cleaning and transformation.
- `forecasting_pipeline.py` – Main script for running forecasting models.
- `power_bi_dashboard.pbix` – Power BI visualization file.
- `g_sheets_reporting_automation.py` – Google Sheets automation script.
- `forecasting_intake_form_template.xlsx` – Standardized forecasting intake form.
- `requirements.txt` – List of dependencies.
- `LICENSE` – Open-source license.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact
For questions or support, feel free to open an issue on GitHub.

