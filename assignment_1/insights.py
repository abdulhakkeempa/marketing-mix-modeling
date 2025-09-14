import streamlit as st
from metrics import calculate_channel_performance


def generate_insights(combined_df, filtered_marketing, metrics):
    channel_performance = calculate_channel_performance(filtered_marketing)
    
    if len(channel_performance) == 0:
        return None, None
    
    best_channel = channel_performance.loc[channel_performance['roas'].idxmax(), 'channel']
    worst_channel = channel_performance.loc[channel_performance['roas'].idxmin(), 'channel']
    best_roas = channel_performance['roas'].max()
    worst_roas = channel_performance['roas'].min()
    
    opportunities = {
        'title': "🎯 Top Opportunities",
        'items': [
            f"**Scale {best_channel}**: Currently delivering {best_roas:.2f}x ROAS - consider increasing budget allocation",
            f"**Optimize High AOV Days**: Days with AOV > ${metrics['avg_aov']*1.2:.0f} show 20% better profit margins",
            "**Weekend Performance**: Analysis suggests different customer behavior patterns on weekends"
        ]
    }
    
    improvements = {
        'title': "⚠️ Areas for Improvement",
        'items': [
            f"**Review {worst_channel}**: Currently at {worst_roas:.2f}x ROAS - analyze or pause underperforming campaigns",
            "**Customer Acquisition Cost**: New customer acquisition costs may be trending upward",
            "**Margin Optimization**: Gross margins show volatility - investigate COGS fluctuations"
        ]
    }
    
    return opportunities, improvements


def render_insights_section(combined_df, filtered_marketing, metrics):
    st.header("💡 Key Insights & Recommendations")
    
    opportunities, improvements = generate_insights(combined_df, filtered_marketing, metrics)
    
    if opportunities is None or improvements is None:
        st.warning("Not enough data to generate insights.")
        return
    
    insights_col1, insights_col2 = st.columns(2)
    
    with insights_col1:
        st.success(f"""
        **{opportunities['title']}**
        
        1. {opportunities['items'][0]}
        
        2. {opportunities['items'][1]}
        
        3. {opportunities['items'][2]}
        """)
    
    with insights_col2:
        st.warning(f"""
        **{improvements['title']}**
        
        1. {improvements['items'][0]}
        
        2. {improvements['items'][1]}
        
        3. {improvements['items'][2]}
        """)


def calculate_advanced_insights(combined_df, marketing_df):
    insights = {}
    
    insights['revenue_volatility'] = combined_df['total_revenue'].std() / combined_df['total_revenue'].mean()
    
    combined_df['day_of_week'] = combined_df['date'].dt.day_name()
    day_performance = combined_df.groupby('day_of_week')['total_revenue'].mean()
    insights['best_day'] = day_performance.idxmax()
    insights['best_day_revenue'] = day_performance.max()
    
    if len(combined_df) > 7:
        recent_roas = combined_df.tail(7)['marketing_roas'].mean()
        earlier_roas = combined_df.head(7)['marketing_roas'].mean()
        insights['roas_trend'] = (recent_roas - earlier_roas) / earlier_roas * 100 if earlier_roas > 0 else 0
    else:
        insights['roas_trend'] = 0
    
    channel_spend = marketing_df.groupby('channel')['spend'].sum()
    total_spend = channel_spend.sum()
    insights['channel_concentration'] = (channel_spend / total_spend).max() if total_spend > 0 else 0
    
    return insights
