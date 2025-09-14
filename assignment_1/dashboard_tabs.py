import streamlit as st
from metrics import (
    calculate_channel_performance, 
    calculate_campaign_performance, 
    calculate_tactic_performance,
    format_metrics_for_display
)
from visualizations import (
    create_performance_trends_chart,
    create_channel_roas_chart,
    create_spend_allocation_chart,
    create_margin_trend_chart,
    create_cost_breakdown_chart,
    create_efficiency_scatter_chart,
    create_tactic_performance_chart
)


def render_performance_trends_tab(combined_df):    
    st.subheader("Business Performance Over Time")
    
    fig = create_performance_trends_chart(combined_df)
    st.plotly_chart(fig, use_container_width=True)


def render_channel_analysis_tab(filtered_marketing):    
    st.subheader("Marketing Channel Performance")
    
    channel_performance = calculate_channel_performance(filtered_marketing)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_roas = create_channel_roas_chart(channel_performance)
        st.plotly_chart(fig_roas, use_container_width=True)
    
    with col2:
        fig_spend = create_spend_allocation_chart(channel_performance)
        st.plotly_chart(fig_spend, use_container_width=True)
    
    st.subheader("Detailed Channel Metrics")
    
    format_config = {
        'spend': 'currency',
        'attributed_revenue': 'currency',
        'roas': 'multiplier',
        'ctr': 'percentage',
        'cpc': 'currency'
    }
    
    display_df = format_metrics_for_display(channel_performance, format_config)
    display_df.columns = ['Channel', 'Total Spend', 'Attributed Revenue', 'Clicks', 'Impressions', 'ROAS', 'CTR', 'CPC']
    st.dataframe(display_df, use_container_width=True)


def render_profitability_tab(combined_df, metrics):    
    st.subheader("Profitability Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_margin = create_margin_trend_chart(combined_df)
        st.plotly_chart(fig_margin, use_container_width=True)
    
    with col2:
        fig_costs = create_cost_breakdown_chart(metrics, combined_df)
        st.plotly_chart(fig_costs, use_container_width=True)
    
    st.subheader("Marketing Efficiency Analysis")
    
    fig_efficiency = create_efficiency_scatter_chart(combined_df)
    st.plotly_chart(fig_efficiency, use_container_width=True)


def render_campaign_details_tab(filtered_marketing):    
    st.subheader("Campaign Performance Details")
    campaign_performance = calculate_campaign_performance(filtered_marketing)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**🏆 Top 10 Campaigns by ROAS**")
        top_campaigns = campaign_performance.head(10).copy()
        
        format_config = {
            'spend': 'currency',
            'attributed_revenue': 'currency',
            'roas': 'multiplier'
        }
        
        top_campaigns_formatted = format_metrics_for_display(top_campaigns, format_config)
        st.dataframe(
            top_campaigns_formatted[['channel', 'campaign', 'spend', 'attributed_revenue', 'roas']],
            use_container_width=True
        )
    
    with col2:
        st.write("**📉 Bottom 10 Campaigns by ROAS**")
        bottom_campaigns = campaign_performance.tail(10).copy()
        
        bottom_campaigns_formatted = format_metrics_for_display(bottom_campaigns, format_config)
        st.dataframe(
            bottom_campaigns_formatted[['channel', 'campaign', 'spend', 'attributed_revenue', 'roas']],
            use_container_width=True
        )
    
    st.subheader("Performance by Ad Tactic")
    
    tactic_performance = calculate_tactic_performance(filtered_marketing)
    fig_tactics = create_tactic_performance_chart(tactic_performance)
    st.plotly_chart(fig_tactics, use_container_width=True)
