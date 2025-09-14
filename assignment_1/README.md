# E-commerce Marketing Analytics Dashboard

A modular and well-organized Streamlit dashboard for analyzing e-commerce marketing performance.

## Project Structure

```
assignment_1/
├── main.py                 # Main dashboard application
├── config.py              # Configuration settings and constants
├── data_loader.py          # Data loading and preparation functions
├── metrics.py              # Metrics calculation functions
├── visualizations.py       # Chart and plot creation functions
├── dashboard_tabs.py       # Individual tab content rendering
├── insights.py             # Insights and recommendations generation
├── __init__.py            # Package initialization
├── README.md              # This file
├── requirements.py         # Dependencies (legacy)
├── ecommerce_dashboard.py  # Original monolithic version
└── dataset/               # Data files
    ├── business.csv
    ├── Facebook.csv
    ├── Google.csv
    └── TikTok.csv
```

## Module Descriptions

### `main.py`
- Main entry point for the dashboard
- Orchestrates all components
- Handles page setup and layout
- Coordinates data flow between modules

### `config.py`
- Configuration settings and constants
- Page configuration for Streamlit
- CSS styles
- Color schemes
- Data file mappings
- Column name mappings

### `data_loader.py`
- Data loading from CSV files
- Data cleaning and preparation
- Column renaming and standardization
- Data validation and error handling

### `metrics.py`
- Business metrics calculations
- Marketing performance metrics
- KPI computations
- Data aggregation functions
- Metrics formatting utilities

### `visualizations.py`
- Chart and plot creation using Plotly
- Reusable visualization functions
- Chart styling and configuration
- Interactive plot generation

### `dashboard_tabs.py`
- Content rendering for each dashboard tab
- Tab-specific layout and components
- Data table formatting
- Tab coordination

### `insights.py`
- Automated insights generation
- Recommendations based on data analysis
- Advanced analytics functions
- Performance trend analysis

## Running the Dashboard

To run the modular dashboard:

```bash
cd assignment_1
streamlit run main.py
```

## Benefits of Modular Structure

1. **Maintainability**: Each module has a single responsibility
2. **Reusability**: Functions can be reused across different parts
3. **Testing**: Each module can be tested independently
4. **Collaboration**: Multiple developers can work on different modules
5. **Scalability**: Easy to add new features and tabs
6. **Debugging**: Issues can be isolated to specific modules

## Adding New Features

### Adding a New Tab
1. Create the tab rendering function in `dashboard_tabs.py`
2. Add any required visualizations to `visualizations.py`
3. Add the tab to the main tabs list in `main.py`

### Adding New Metrics
1. Add calculation functions to `metrics.py`
2. Update visualizations if needed in `visualizations.py`
3. Include in relevant tabs in `dashboard_tabs.py`

### Adding New Insights
1. Add analysis functions to `insights.py`
2. Update the insights rendering in `insights.py`

## Data Requirements

The dashboard expects CSV files in the `dataset/` folder with the following structure:

### business.csv
- date, # of orders, # of new orders, new customers, total revenue, gross profit, COGS

### Facebook.csv, Google.csv, TikTok.csv
- date, tactic, state, campaign, impression, clicks, spend, attributed revenue
