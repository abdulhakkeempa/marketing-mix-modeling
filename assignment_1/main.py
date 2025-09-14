import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import warnings

from config import PAGE_CONFIG, CUSTOM_CSS, TIME_PERIODS
from data_loader import load_data, prepare_data, get_data_info
from metrics import calculate_metrics, create_executive_metrics
from dashboard_tabs import (
    render_performance_trends_tab,
    render_channel_analysis_tab,
    render_profitability_tab,
    render_campaign_details_tab
)
from insights import render_insights_section

warnings.filterwarnings('ignore')


def setup_page():
    st.set_page_config(**PAGE_CONFIG)
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def render_header():
    st.title("📊 E-commerce Marketing Analytics Dashboard")
    st.markdown("*Strategic insights for data-driven decision making*")

def create_sidebar_filters(business_df, marketing_df):
    st.sidebar.header("📊 Dashboard Filters")
    st.sidebar.subheader("📅 Filters")
    
    date_options = {}
    for period_name, days in TIME_PERIODS.items():
        if days is None:
            date_options[period_name] = business_df['date'].min()
        else:
            date_options[period_name] = datetime.now() - timedelta(days=days)
    
    selected_period = st.sidebar.selectbox("Time Period", list(date_options.keys()), index=2)
    date_filter = date_options[selected_period]
    
    channels = ['All'] + sorted(marketing_df['channel'].unique().tolist())
    selected_channel = st.sidebar.selectbox("Marketing Channel", channels)
    
    return date_filter, selected_channel


def render_executive_summary(metrics):
    st.header("🎯 Executive Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Revenue",
            value=f"${metrics['total_revenue']:,.0f}",
            delta=f"{metrics['revenue_growth']:+.1f}%"
        )
    
    with col2:
        st.metric(
            label="Marketing ROAS",
            value=f"{metrics['overall_roas']:.2f}x",
            delta="Return on Ad Spend"
        )
    
    with col3:
        st.metric(
            label="Average Order Value",
            value=f"${metrics['avg_aov']:.2f}",
            delta=f"{metrics['total_orders']:,} orders"
        )
    
    with col4:
        st.metric(
            label="Gross Margin",
            value=f"{metrics['gross_margin']:.1f}%",
            delta=f"${metrics['total_spend']:,.0f} ad spend"
        )


def render_dashboard_tabs(combined_df, filtered_marketing, metrics):
    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Performance Trends", 
        "🎯 Channel Analysis", 
        "💰 Profitability", 
        "🔍 Campaign Details"
    ])
    
    with tab1:
        render_performance_trends_tab(combined_df)
    
    with tab2:
        render_channel_analysis_tab(filtered_marketing)
    
    with tab3:
        render_profitability_tab(combined_df, metrics)
    
    with tab4:
        render_campaign_details_tab(filtered_marketing)


def main():
    """Main dashboard application"""
    
    setup_page()
    
    render_header()
    
    with st.spinner('Loading data from dataset folder...'):
        business_df, marketing_df = load_data()
    
    if business_df is None or marketing_df is None:
        st.error("Failed to load data. Please check that the dataset folder contains the required CSV files.")
        return
    
    business_df, marketing_df = prepare_data(business_df, marketing_df)
    
    data_info = get_data_info(business_df, marketing_df)
    # st.success(f"✅ Data loaded successfully! Business data: {data_info['business_records']} records, Marketing data: {data_info['marketing_records']} records")
    
    date_filter, selected_channel = create_sidebar_filters(business_df, marketing_df)
    
    combined_df, filtered_marketing = calculate_metrics(
        business_df, marketing_df, date_filter, selected_channel
    )
    
    metrics = create_executive_metrics(combined_df, filtered_marketing)
    
    # Render executive summary
    render_executive_summary(metrics)
    
    # Render dashboard tabs
    render_dashboard_tabs(combined_df, filtered_marketing, metrics)
    
    # Render insights and recommendations
    render_insights_section(combined_df, filtered_marketing, metrics)


if __name__ == "__main__":
    main()
