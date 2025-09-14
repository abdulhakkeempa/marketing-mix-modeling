import pandas as pd
import numpy as np


def calculate_metrics(business_df, marketing_df, date_filter=None, channel_filter=None):
    if date_filter:
        business_df = business_df[business_df['date'] >= date_filter]
        marketing_df = marketing_df[marketing_df['date'] >= date_filter]
    
    if channel_filter and channel_filter != 'All':
        marketing_df = marketing_df[marketing_df['channel'] == channel_filter]
    
    marketing_daily = marketing_df.groupby('date').agg({
        'spend': 'sum',
        'clicks': 'sum',
        'impression': 'sum',
        'attributed_revenue': 'sum'
    }).reset_index()
    
    combined_df = pd.merge(business_df, marketing_daily, on='date', how='left')
    combined_df = combined_df.fillna(0)
    
    # Calculate derived metrics
    combined_df['marketing_roas'] = combined_df['attributed_revenue'] / combined_df['spend'].replace(0, np.nan)
    combined_df['ctr'] = combined_df['clicks'] / combined_df['impression'].replace(0, np.nan)
    combined_df['cpc'] = combined_df['spend'] / combined_df['clicks'].replace(0, np.nan)
    combined_df['gross_margin'] = combined_df['gross_profit'] / combined_df['total_revenue'].replace(0, np.nan)
    combined_df['aov'] = combined_df['total_revenue'] / combined_df['no_of_orders'].replace(0, np.nan)
    combined_df['new_customer_rate'] = combined_df['new_customers'] / combined_df['no_of_orders'].replace(0, np.nan)
    
    return combined_df, marketing_df


def create_executive_metrics(combined_df, marketing_df):
    total_revenue = combined_df['total_revenue'].sum()
    total_spend = combined_df['spend'].sum()
    total_orders = combined_df['no_of_orders'].sum()
    total_customers = combined_df['new_customers'].sum()
    
    overall_roas = total_spend > 0 and combined_df['attributed_revenue'].sum() / total_spend or 0
    avg_aov = total_orders > 0 and total_revenue / total_orders or 0
    gross_margin = total_revenue > 0 and combined_df['gross_profit'].sum() / total_revenue or 0
    
    mid_point = len(combined_df) // 2
    recent_revenue = combined_df.iloc[mid_point:]['total_revenue'].mean()
    earlier_revenue = combined_df.iloc[:mid_point]['total_revenue'].mean()
    revenue_growth = (recent_revenue - earlier_revenue) / earlier_revenue * 100 if earlier_revenue > 0 else 0
    
    return {
        'total_revenue': total_revenue,
        'total_spend': total_spend,
        'overall_roas': overall_roas,
        'avg_aov': avg_aov,
        'gross_margin': gross_margin * 100,
        'revenue_growth': revenue_growth,
        'total_orders': total_orders,
        'total_customers': total_customers
    }


def calculate_channel_performance(marketing_df):    
    channel_performance = marketing_df.groupby('channel').agg({
        'spend': 'sum',
        'attributed_revenue': 'sum',
        'clicks': 'sum',
        'impression': 'sum'
    }).reset_index()
    
    channel_performance['roas'] = channel_performance['attributed_revenue'] / channel_performance['spend']
    channel_performance['ctr'] = np.where(
        channel_performance['impression'] > 0,
        channel_performance['clicks'] / channel_performance['impression'] * 100,
        0
    )
    channel_performance['cpc'] = np.where(
        channel_performance['clicks'] > 0,
        channel_performance['spend'] / channel_performance['clicks'],
        0
    )
    
    return channel_performance


def calculate_campaign_performance(marketing_df):    
    campaign_performance = marketing_df.groupby(['channel', 'campaign']).agg({
        'spend': 'sum',
        'attributed_revenue': 'sum',
        'clicks': 'sum',
        'impression': 'sum'
    }).reset_index()
    
    campaign_performance['roas'] = campaign_performance['attributed_revenue'] / campaign_performance['spend']
    campaign_performance = campaign_performance.sort_values('roas', ascending=False)
    
    return campaign_performance


def calculate_tactic_performance(marketing_df):    
    tactic_performance = marketing_df.groupby(['channel', 'tactic']).agg({
        'spend': 'sum',
        'attributed_revenue': 'sum',
        'clicks': 'sum',
        'impression': 'sum'
    }).reset_index()
    
    tactic_performance['roas'] = tactic_performance['attributed_revenue'] / tactic_performance['spend']
    tactic_performance['ctr'] = tactic_performance['clicks'] / tactic_performance['impression'] * 100
    
    return tactic_performance


def format_metrics_for_display(df, columns_to_format):    
    display_df = df.copy()
    
    for col, format_type in columns_to_format.items():
        if col in display_df.columns:
            if format_type == 'currency':
                display_df[col] = display_df[col].apply(lambda x: f"${x:,.0f}")
            elif format_type == 'percentage':
                display_df[col] = display_df[col].apply(lambda x: f"{x:.2f}%")
            elif format_type == 'multiplier':
                display_df[col] = display_df[col].apply(lambda x: f"{x:.2f}x")
    
    return display_df
