# Page configuration
PAGE_CONFIG = {
    "page_title": "E-commerce Marketing Analytics Dashboard",
    "page_icon": "📊",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Custom CSS styles
CUSTOM_CSS = """
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .big-font {
        font-size: 24px !important;
        font-weight: bold;
    }
    .medium-font {
        font-size: 18px !important;
        font-weight: bold;
    }
</style>
"""

# Data file mappings
DATA_FILES = {
    'business': 'business.csv',
    'marketing': {
        'Facebook': 'Facebook.csv',
        'Google': 'Google.csv',
        'TikTok': 'TikTok.csv'
    }
}

# Column name mappings for data cleaning
COLUMN_MAPPINGS = {
    'business': {
        '# of orders': 'no_of_orders',
        'new customers': 'new_customers',
        '# of new orders': 'no_of_new_orders',
        "total revenue": "total_revenue",
        "gross profit": "gross_profit"
    },
    'marketing': {
        'attributed revenue': 'attributed_revenue'
    }
}

# Chart color schemes
COLORS = {
    'revenue': '#2E8B57',
    'spend': '#FF6B6B',
    'roas': '#4ECDC4',
    'orders': '#45B7D1',
    'new_orders': '#96CEB4',
    'customers': '#FFEAA7',
    'income': '#2E8B57',
    'cost': '#FF6B6B'
}

# Time period options
TIME_PERIODS = {
    'Last 7 Days': 7,
    'Last 30 Days': 30,
    'Last 90 Days': 90,
    'All Time': None
}
